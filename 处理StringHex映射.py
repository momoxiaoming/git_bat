# coding:utf-8
import os

mapFile = './file/map.txt'
path = "D:/zhangjinming/work/git/open-group/ng/open-scenes/" + "src/main/java"

def getAllDir(path,files=[]):

    list = os.listdir(path)
    for item in list:
        itemPath=path+"/"+item
        if os.path.isdir(itemPath):
            getAllDir(itemPath,files)
        else:
            files.append(itemPath) #文件,需要保存

    return files
def getMap():
    file=open(mapFile,'r',encoding='UTF-8')
    hList=file.readlines()
    list=[]
    for item in hList:
        map = {}
        sp=item.strip().split(":")
        key=sp[0].strip()
        value=sp[1].strip()
        map[key]=value
        list.append(map)

    print(list)


def dumpFile():
    for item in getAllDir(path):
        fileContent=open(item).read()







if __name__ == '__main__':
    getMap()
    # list=getAllDir(path)
    # print(list)
