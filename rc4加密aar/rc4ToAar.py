import os
import subprocess

import arc4
import requests
import hashlib
import zipfile




aar_version = '1.108.3.240730.1'

rc4_key = 'good_hot_dex'
baseDir='aar/'


def unzip(zip_file):
    target_folder = './'+zip_file.replace(".aar", '')
    # 打开 ZIP 文件
    f = zipfile.ZipFile(zip_file, 'r')
    for file in f.namelist():
        f.extract(file, target_folder)
    f.close()
    return target_folder + "/classes.jar"


def mdgString(text):
    md5 = hashlib.md5()
    # 更新哈希对象以包含字符串的字节表示
    md5.update(text.encode('utf-8'))
    # 计算哈希值并以十六进制字符串形式返回
    return md5.hexdigest()


def jumpArrToDex():
    header = {'Accept-Encoding': 'gzip, deflate', 'Authorization': 'Basic dmFwcC1yZWFkZXI6cHdkMTIzNDU2'}
    aar_path = 'http://dnsdk.vimedia.cn:8081/repository/Viapp-release/com/dn/group/ng/eazy-scenes/' + aar_version + '/eazy-scenes-' + aar_version + '.aar'
    print("aar_path:"+aar_path)
    response = requests.get(aar_path, headers=header)
    spList = aar_path.split('/')
    name = spList[spList.__len__() - 1]
    fileName = baseDir + name
    with open(fileName, 'wb') as f:
        f.write(response.content)
    classFile = unzip(fileName)
    dexPath = jarToDex(classFile)
    outFile=aar_version.replace(".",'')
    encrypt(rc4_key, dexPath, dexPath.replace('classes.dex', outFile))
    os.remove(fileName)

def jarToDex(jarPath):
    """
    将jar文件转dex,
    :return:
    """
    aarDir = jarPath.replace('classes.jar', 'classes.dex')
    command = 'dx --dex --output ' + aarDir + ' ' + jarPath
    subprocess.run(command, shell=True)
    return aarDir


def encrypt(key, inputFile, outFile):
    with open(inputFile, "rb") as f:
        data = f.read()

    # 创建 RC4 加密器对象
    cipher = arc4.ARC4(key)

    encrypted_data = cipher.encrypt(data)

    with open(outFile, "wb") as f:
        f.write(encrypted_data)


def dcodecrypt(key, inputFile, outFile):
    with open(inputFile, "rb") as f:
        data = f.read()

    # 创建 RC4 加密器对象
    cipher = arc4.ARC4(key)

    encrypted_data = cipher.enddcrypt(data)

    with open(outFile, "wb") as f:
        f.write(encrypted_data)


if __name__ == '__main__':

    # 密钥
    jumpArrToDex()
