import json
import os


def getBuildInfos():
    """
    获取test_phone_info.json中所有的正常机型信息,
    :return:
    """
    with open('info/test_phone_info.json', 'r') as file:
        data = json.load(file)

    if len(data) < 1:
        raise Exception('数据量不足,无法对比')
    temp = None
    for item in data:
        if temp is None:
            temp = item
        temp = contrastInfo(temp, item)
    print(temp)


def contrastInfo(temp, item):
    keys = item.keys()
    rlt = {}
    for key in keys:
        if temp.get(key) == item.get(key) and item.get(key) != None:
            rlt[key] = item[key]
    return rlt



def jumpAuditInfo():
    """
    解析审核数据
    :return:
    """
    with open('info/audit_phone_info.json', 'r') as file:
        lines = file.readlines()
    for line in lines:
        data=json.loads(line)
        data=data["build"]
        data=json.loads(data)
        print("\n")
        if not isRiskInfo(data):
            print("危险数据->"+str(data))


def isRiskInfo(item):
    """
    比较安全json字段, 判断当前数据是否安全
    :param item:
    :return:
    """
    rlt=True
    with open('info/phone.json', 'r') as file:
        data = json.load(file)
    for key in data.keys():
        if item.get(key) is not None and not str(item[key]).__contains__(str(data[key])):
            print("risk--"+key+" : "+str(data[key])+" ? "+str(item.get(key)))
            rlt=False
    return rlt

if __name__ == '__main__':
    getBuildInfos()
    # jumpAuditInfo()