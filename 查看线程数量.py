#coding:utf-8

import os
import time


def cmd(cmd):
    b = os.popen(cmd).read()
    if b.__contains__("error"):
        raise RuntimeError('命令出错,中断运行')
    return b

def cmdRun():

    for i in range(0,1000):
        rlt = cmd('adb shell ps | grep cn.inandroidhwu.umctstech')
        print('线程数量-->' + rlt)
        time.sleep(1000)




if __name__ == '__main__':
    cmdRun()
