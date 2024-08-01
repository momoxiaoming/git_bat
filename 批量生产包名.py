import os
import random

KEY=["cts",'google','vivo','oppo','mc','mckj','dn','hw']  #包名排除的关键词
START="com"         #包名前缀
PKG_LEN=range(3,7)  #生成的包名,每串长度范围


def randmCha():
    return chr(random.randint(ord('a'), ord('z')))

def randStr(num):
    str=""
    for i in range(0,num):
        str+=randmCha()

    return str

def randStrForKey(num):
    str=randStr(num)
    rlt=True
    for i in KEY:
        if str.__contains__(i):
            rlt=False
            break

    if not rlt:
        return randStrForKey(num)
    else:
        return str


def randNumStr(start,end):
    """
    随机生成start位到end位的字符串
    :param start:
    :param end:
    :return:
    """
    num=random.randint(start,end)
    return randStrForKey(num)

def randPackage(listNum):
    list=[]
    for i in range(0,listNum):
        pkg = START+"."+ randNumStr(PKG_LEN.start, PKG_LEN.stop) + "." + randNumStr(PKG_LEN.start, PKG_LEN.stop) + "." + randNumStr(PKG_LEN.start, PKG_LEN.stop)
        list.append(pkg)
    return list

def saveListToTxt(list):
    # 单层列表写入文件
    file=open("data.txt", "w")
    for i in list:
        file.writelines(i+"\n")

if __name__ == '__main__':
    list=randPackage(100)
    saveListToTxt(list)
