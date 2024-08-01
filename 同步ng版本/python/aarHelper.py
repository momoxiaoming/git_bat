import io
import os
import sys
import json

jsonFilePath="../modules/default_common_depend.json"
config_dnapp="../modules/config-dnapp.gradle"
config_gradle="../modules/config.gradle"
version_txt="./aarHelper.txt"
platform_txt="../modules/default_platform_depend.json"

def readVersionText():
    """
    读取aar版本文件,,替换config以及json
    :return:
    """
    aarMap={}
    data=open(version_txt,'rb+')
    lines=data.readlines()
    for line in lines:
        lineStr=str(line,'utf-8').replace(" ", "").replace("\n", '').replace("\r", '').replace("\"", "").replace("\'","")
        if lineStr.startswith("//") or lineStr.startswith("#") or not lineStr.__contains__("="):
            continue
        else:
            split=lineStr.split("=")
            if split.__len__() == 2:
                aar=split[1].replace('\"',"")
                aarName=aar.split(":")
                aarMap[aarName[0]+":"+aarName[1]+":"]=aarName[2]
    return aarMap


def replaceJsonFile(aarMap):
    """
    根据得到的版本,替换json文件中对应的版本
    :param aarMap:
    :return:
    """
    fileIn = open(jsonFilePath)
    fileContent = fileIn.read()
    jsonData = json.loads(str(fileContent))
    fileText=str(fileContent)
    # 找出所有需要替换的aar
    libs_module = getReplaceAAr(jsonData['libs_module'], aarMap)
    libs_ng = getReplaceAAr(jsonData['libs_ng'], aarMap)
    aar_list = list(libs_module).__add__(libs_ng)
    for aar in aar_list:
        # 得到替换后的aar版本
        split = aar.split(":")
        name = split[0] + ':' + split[1] + ':'
        newAAR = name + aarMap[name]
        # print(aar+'--->'+newAAR)
        fileText=fileText.replace(aar,newAAR)
    # print(fileText)

    fileIn.close()
    """
    最后更新json文件
    """
    fileW = open(jsonFilePath,'w')
    fileW.write(str(fileText))
    fileW.close()
    # fileIn.flush()

    print("default_common_depend.json 替换成功")


def replacePlatformJsonFile(aarMap):
    """
    根据得到的版本,替换replacePlatformJsonFile文件中对应的版本
    :param aarMap:
    :return:
    """
    fileIn = open(platform_txt)
    fileContent = fileIn.read()
    jsonData = json.loads(str(fileContent))
    fileText=str(fileContent)
    # 找出所有需要替换的aar
    libs_base = getReplaceAAr(jsonData['libs_base'], aarMap)
    libs_ad = getReplaceAAr(jsonData['libs_ad'], aarMap)
    libs_tj = getReplaceAAr(jsonData['libs_tj'], aarMap)
    libs_track = getReplaceAAr(jsonData['libs_track'], aarMap)
    aar_list = list(libs_base).__add__(libs_ad).__add__(libs_tj).__add__(libs_track)
    for aar in aar_list:
        # 得到替换后的aar版本
        split = aar.split(":")
        name = split[0] + ':' + split[1] + ':'
        newAAR = name + aarMap[name]
        # print(aar+'--->'+newAAR)
        fileText=fileText.replace(aar,newAAR)
    # print(fileText)

    fileIn.close()
    """
    最后更新json文件
    """
    fileW = open(platform_txt,'w')
    fileW.write(str(fileText))
    fileW.close()
    # fileIn.flush()

    print("default_platform_depend.json 替换成功")

def replaceConfgFile(aarMap):
    """
    替换config.gradle文件中的版本
    :return:
    """
    file=open(config_gradle,'rb+')
    lines = file.readlines()
    file.close()
    file2=open(config_gradle,'rb+')
    content=str(file2.read(),'utf-8')
    file2.close()
    map={}
    for key in aarMap.keys():
        for line in lines:
            line_str=str(line,'utf-8').replace(" ", "").replace("\n", '').replace("\r", '').replace("\"", "")
            tains=str(key).replace("\'","").replace("\"",'')
            if line_str.__contains__(tains):
                split=line_str.split("=")
                # newStr=split[0]+'='+key+aarMap[key]
                # content=content.replace(line_str,newStr)
                map[split[0]]=key+aarMap[key]

    # print(map)
    # print(content)
    aar_lines=content.split('\n')
    new_aar_lines=[]
    for line in aar_lines:
        if line.__contains__("="):
            split = line.split("=")
            key=split[0].replace(" ","")
            aarText=split[1].replace("\"","\'")
            if map.keys().__contains__(key):
                mapKey=map[key].replace("\'","").replace("\"","")
                tj = aarText.split("\'")
                newLine = split[0] + "=" + tj[0] +"\""+mapKey+"\""+tj[2]
                # print(newLine)
                new_aar_lines.append(newLine)
            else:
                new_aar_lines.append(line)
        else:
            new_aar_lines.append(line)

    # print(new_aar_lines)

    file3 = open(config_gradle, 'wb+')

    new_aar_str=""
    for line in new_aar_lines:
        if new_aar_lines[new_aar_lines.__len__()-1]==line:
            new_aar_str = new_aar_str + line
        else:
            new_aar_str = new_aar_str + line + "\n"

    # print(new_aar_str)
    encodeData=new_aar_str.encode()
    file3.write(encodeData)
    file3.close()
    print("config.gradle 替换成功")



def getReplaceAAr(list, aarMap):
    apArr = []
    for data in list:
        path = data['path']
        aarList = str(path).split('#')
        for aar in aarList:
            split = aar.split(':')
            name = split[0] + ':' + split[1] + ':'
            if aarMap.keys().__contains__(name):
                # print(name)
                apArr.append(aar)
    return apArr

def test():
    print("test")
if __name__ == "__main__":
    map = readVersionText()
    replaceJsonFile(map)
    replacePlatformJsonFile(map)
    replaceConfgFile(map)
