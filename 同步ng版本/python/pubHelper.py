import io
import os
import json
jsonFilePath="../modules/default_common_depend.json"
config_dnapp="../publish/config-dnapp.gradle"
config_gradle="../modules/config.gradle"

def readDnappVer():
    """
    读取config-dnapp.gradle中版本
    需要以下数据
    ng_group_id
    ng_version
    aar_version
    artifact_id
    :return:
    """
    dnapp = open(config_dnapp, 'rb')
    lines = dnapp.readlines()
    verDir = {}
    for i in lines:
        line = str(i, 'utf-8').replace(" ", "")
        if line.__contains__("=") and not line.startswith("//"):
            split = line.split("=")
            key = str(split[0])
            value = str(split[1])
            verDir[key.replace('\n', '')] = value.replace("\n", '').replace("\r", '').replace("\"", "")

    ng_group_id = verDir['ng_group_id']
    ng_version = verDir['ng_version']
    aar_version = {}
    artifact_ids = {}
    aarMap = {}

    for key in verDir.keys():
        if key.__contains__("_id") and key != 'ng_group_id':
            artifact_ids[key] = verDir[key]
        if key.__contains__("_version") and key != 'ng_version':
            value = verDir[key]
            if value == 'ng_version':
                aar_version[key] = ng_version
            else:
                aar_version[key] = verDir[key]

    for value in verDir.values():
        if value.__contains__(":$"):
            split = value.replace('$', "").split(':')
            artifact = split[1]
            version = split[2]
            aar = str(ng_group_id + ':' + artifact_ids[artifact] + ':')
            aarMap[aar] = aar_version[version]
    # print(aarMap)
    print("config-dnapp.gradle 版本读取成功")


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
            if line_str.__contains__(key):
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
            if map.keys().__contains__(key):
                tj = split[1].split("\"")
                newLine = split[0] + "=" + tj[0] +"\""+map[key]+"\""+tj[2]
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


if __name__ == "__main__":
    map = readDnappVer()
    replaceJsonFile(map)
    replaceConfgFile(map)
