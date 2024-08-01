import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json


def readXlsxFile(filepath, column, sheet_name="Sheet1"):
    """
    读取xlsx文件中某一列的数据
    :param filepath: 文件路径
    :param column: 列名称
    :param sheet_name: 表名
    :return:
    """
    data = pd.read_excel(filepath, sheet_name=sheet_name)
    list = []
    for row in data.iloc:
        risk = row[column]
        list.append(risk)
    return list


def checkRisk(repo, keyObjList):
    index = 0
    for i in repo:
        item = str(i)
        for keyObj in keyObjList:
            key = next(iter(keyObj))
            value_list = keyObj[key]
            risk = False
            for va in value_list:
                if item.__contains__(va):
                    # 符合过滤,
                    js = json.loads(item)
                    data = js.get(key)
                    if str(data).__contains__(va):
                        risk = True
                        break

            if risk:
                index += 1
                # print(item)
                break
    mc = round((index / len(repo)) * 100, 3)
    print("总数:" + str(len(repo)) + " 匹配数:" + str(index) + " 匹配率:" + str(mc) + "%")
    return [index,len(repo)-index]


if __name__ == '__main__':
    list = readXlsxFile('./risk_env_init.build无筛选.xlsx', "risk_env_init的build子参（无筛选）")
    risk = [
        {"DISPLAY": ["dev-key"]},
        {"FINGERPRINT": ["test-key", "dev-keys"]},
        {"HOST": ["google.com"]},
        {"TYPE": ["debug", "eng"]},
        {"IS_EMULATOR": ["true"]},
        {"TAGS": ["test-keys"]},
        {"IS_DEBUGGABLE": ["true"]},

    ]
    ret=checkRisk(list, risk)
    y = np.array(ret)
    plt.pie(y,
            labels=['risk', 'safe'],  # 设置饼图标签
            colors=["#d5695d", "#5d8ca8"],  # 设置饼图颜色
            explode=(0, 0),  # 第二部分突出显示，值越大，距离中心越远
            autopct='%.2f%%',  # 格式化输出百分比
            )
    plt.title("build data")
    plt.show()
