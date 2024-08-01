import io
import os
import shutil
import sys
import json
import time


def findDirForTime(path):
    """
    查找某个目录下所有某个时间的文件夹,过滤掉.开头的隐藏文件夹
    :return:
    """
    listDir = []
    dirs = os.listdir(path)
    for dir in dirs:
        filePath = path + dir
        if not os.path.isfile(filePath) and not dir.startswith("."):
            listDir.append(filePath)
    return listDir

def deleteDirForTime(dirFile,invTime):
    """
    删除某个日期前文件夹
    :return:
    """
    fileTime = os.path.getmtime(dirFile)
    nowTime = time.time()
    if (float(nowTime) - float(fileTime)) >= invTime:
        shutil.rmtree(dirFile)
        print(str(dirFile)+"----已删除")


def findWorkSpaceDelete(invTime):
    """
    删除工作空间下的过期目录
    :param invTime:
    :return:
    """
    path="jenkins-data/workspace/"
    list2=findDirForTime(path)
    for dir in list2:
        deleteDirForTime(dir,invTime)

def findBuildDelete(invTime):
    """
    删除项目build下过期目录
    :return:
    """
    path="jenkins-data/jobs/"
    list1=findDirForTime(path)
    for dir in list1:
        #builds下查找所有mulu
        roots=findDirForTime(dir+"/builds/")
        for root in roots:
            deleteDirForTime(root,invTime)



if __name__ == '__main__':
    """
    支持传入要删除的目录天数 python3 jenkinsClean.py 15 
    """
    invTime=15 * 24 * 60 * 60
    arg=sys.argv[1:]
    if arg.__len__()>0 and float(arg[0])>0:
        invTime = float(arg[0]) * 24 * 60 * 60
    findWorkSpaceDelete(invTime)
    findBuildDelete(invTime)
    print("执行完毕")
