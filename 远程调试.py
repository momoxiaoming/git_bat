import os
import subprocess
import sys


def adb_shell(cmd):
    # 执行cmd命令，如果成功，返回(0, 'xxx')；如果失败，返回(1, 'xxx')
    res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)  # 使用管道
    result = res.stdout.read()  # 获取输出结果
    res.wait()  # 等待命令执行完成
    res.stdout.close()  # 关闭标准输出
    return result


def cmd(cmd):
    b = os.popen(cmd).read()
    if b.__contains__("error"):
        raise RuntimeError('命令出错,中断运行')
    return b


def connet(port="6666"):
    b = adb_shell('adb shell ifconfig')
    sp = str(b, 'utf-8').replace("\r", "").replace(" ", "").split("\n")
    ip = ""
    for i in sp:
        if i.__contains__("inetaddr:") and not i.__contains__("inetaddr:127.0.0.1"):
            index = i.index("Bcast")
            ip = i[0:index].replace("inetaddr:", "")
            break
    adb_shell('adb tcpip:' + port)
    print(adb_shell('adb connect ' + ip + ":" + port))


def disconnect(port):
    b = adb_shell('adb shell ifconfig')
    sp = str(b, 'utf-8').replace("\r", "").replace(" ", "").split("\n")
    ip = ""
    for i in sp:
        if i.__contains__("inetaddr:") and not i.__contains__("inetaddr:127.0.0.1"):
            index = i.index("Bcast")
            ip = i[0:index].replace("inetaddr:", "")
            break

    print(adb_shell('adb disconnect ' + ip + ":" + port))


if __name__ == '__main__':
    # connet("6666")
    disconnect('6666')