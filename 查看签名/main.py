import os
import subprocess
import sys

from pip._vendor import chardet


def adb_shell(cmd):
    # 执行cmd命令，如果成功，返回(0, 'xxx')；如果失败，返回(1, 'xxx')
    res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)  # 使用管道
    result = res.stdout.read()  # 获取输出结果
    res.wait()  # 等待命令执行完成
    res.stdout.close()  # 关闭标准输出
    return result

def byteToStr(output:bytes):
    encoding = chardet.detect(output)["encoding"]
    s=output.decode(encoding)
    return s

def decodeSHA(outStr,filePath):
    sp = str(byteToStr(outStr)).split('\n')
    map = {}
    ps=str(filePath).split('/')
    name=ps[len(ps)-1]
    map["fileName"]=name
    for i in sp:
        line = i.replace("\n", "").replace("\t", "").replace(" ", '')
        if line.__contains__("SHA1:"):
            map["SHA1"] = i.replace("SHA1:", "").replace("\t", '').replace(" ", '')

        if line.__contains__("SHA256:"):
            map["SHA256"] = i.replace("SHA256:", "").replace("\t", '').replace(" ", '')


    return map

def getJKSSign(apkPath,pwd):
    return decodeSHA(adb_shell("keytool -list -v -keystore "+apkPath+" -storepass "+pwd),apkPath)

def getAabSign(aabPath):
    return decodeSHA(adb_shell("keytool -printcert -jarfile "+aabPath),aabPath)

def getFileSHA(pwd):
    path="./file"
    files=os.listdir(path)
    list=[]
    for i in files:
        lin=path+"/"+i
        if i.endswith('.aab'):
            list.append(getAabSign(lin))
        if i.endswith('.jks') or i.endswith('.keystore'):
            list.append(getJKSSign(lin,pwd))

    return list

if __name__ == '__main__':
    argv=sys.argv[1:]
    if argv.__len__()>0:
        signPwd=argv[0]
        list=getFileSHA(signPwd)
        for i in list:
            print(i)


