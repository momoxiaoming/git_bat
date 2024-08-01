import io
import os


def runObs2():
    """
    倒转,从seed合并mapping,最后返回mapping
    :return:
    """
    mapping = runObs()
    seed = readSeed()
    for key in seed.keys():
        seedList = seed.get(key)
        rlt = False
        # if key.__contains__("androidx.fragment.app.Fragment -> "):
        #     print("yes-->"+key)
        for item in mapping.keys():
            if item.__contains__(key + " -> "):
                # print("包含此class")
                rlt = True
        # print("rlt--->"+str(rlt))
        if rlt == False:
            # mapp中沒有這個类,我们把他加上
            # print("倒转类-->"+key)
            mappList = list()
            for sd in seedList:
                if sd.__contains__("(") and sd.__contains__(")"):
                    # 解析出所有方法
                    arr = sd.split(" ")
                    if len(arr) > 1:
                        rlt = arr[0]
                        nm = arr[1]
                        m = nm.split("(")[0]
                        temp = "    " + rlt + " " + str(nm) + " -> " + m + "\n"

                        mappList.append(temp)
            # print("map---->"+str(mappList))
            clsNum = key + " -> " + key + ":\n"
            # print("缺少的clas-->"+clsNum)
            mapping[clsNum] = mappList
    return mapping


def runObs():
    """
    从mapping合并seed
    :return:
    """
    mapping = readMapping()
    seed = readSeed()
    for key in mapping.keys():
        clsNm = key.split("->")[0].strip()
        seedList = seed.get(clsNm)
        if seedList is None:
            continue
        if len(seedList) > 0:
            # 有保留字段,需要在mapping数组后面添加,优先添加方法
            for sd in seedList:
                if sd.__contains__("(") and sd.__contains__(")"):
                    # 解析出所有方法
                    arr = sd.split(" ")
                    if len(arr) > 1:
                        rlt = arr[0]
                        nm = arr[1]
                        m = nm.split("(")[0]
                        temp = "    " + rlt + " " + str(nm) + " -> " + m + "\n"
                        mappList = mapping.get(key)
                        if not listContains(mappList, nm):
                            mappList.append(temp)
                    # else:

    return mapping


def listContains(list, item):
    for i in list:
        if str(i).__contains__(item):
            return True
    return False


def writeNewMapping():
    path = "./res/newMapping.txt"
    exists = os.path.exists(path)
    if exists:
        os.remove(path)
    map = runObs2()
    file = open(path, 'a+')
    for key in map.keys():
        list = map.get(key)
        file.write(str(key))
        for line in list:
            file.write(str(line))

    print("合并完成")


def writeNewCls():
    path2 = "./res/newCls.txt"
    exists2 = os.path.exists(path2)
    if exists2:
        os.remove(path2)
    map = readMapping()

    newMap = {}
    file2 = open(path2, 'a+')
    for key in map.keys():
        if isContent(key):
            cls = str(key).split('->')[0].strip()
            newCls = cls.split('$')[0].strip()
            newMap[newCls] = "1"

    for key in newMap.keys():
        if not key.endswith("R") or not key.__contains__('-'):
            keep = '-keep class ' + key.strip() + '{*;}\n'
            keep2 = '-keep class ' + key.strip() + '$*{*;}\n'
            file2.write(str(keep))
            file2.write(str(keep2))

    print("合并完成")


def isContent(name):
    cls = ["com.dn.vi",
           "com.mckj",
           "com.tz",
           "com.tencent.mmkv",
           "com.baidu"]

    for item in cls:
        if name.startswith(item):
            return True

    return True


def readSeed():
    """
    读取保留字段
    :return:
    """
    mapping = open("./res/seeds.txt")
    lines = mapping.readlines()
    seedMap = dict()
    for line in lines:
        sp = line.split(":")
        if len(sp) > 1:
            clsNm = sp[0].strip()
            method = sp[1].strip()
            value = seedMap.get(clsNm)
            if value is None:
                value = list()
            value.append(method)
            seedMap[clsNm] = value
    # print(seedMap)
    return seedMap


def filter(line):
    list = ["com.android.tools.r8.GeneratedOutlineSupport", "#", "$"]
    for item in list:
        if line.startswith(item):
            return True
    return False


def readMapping():
    """
    读取mapping 下规则,并归档
    :return:
    """
    mapping = open("./res/mapping.txt")
    lines = mapping.readlines()

    status_invalid = False  # 为true时,此状态之后的缩进行无效
    newMap = dict()
    key = "key"
    for line in lines:
        if filter(line):
            status_invalid = True
            continue
        if line.startswith(" "):
            # 缩进行
            if status_invalid:
                # 无效状态缩进行
                continue
            else:
                # 有效状态缩进
                value = newMap[key]
                value.append(line)
                newMap[key] = value
        else:
            # 非缩进行
            status_invalid = False
            key = line
            newMap[key] = list()

    # print(newMap)
    return newMap


def scanImport():
    path = "D:\\zhangjinming\\work\\git\\GroupApp\\ng\\aos\\src\\main\\java\\com\\m\\c"

    imports = {}
    for root, dirs, files in os.walk(path):
        for f in files:
            content = open(root + "\\" + f,encoding='utf-8')
            for line in content.readlines():
                if line.startswith("import"):
                    pkg=line.replace("import", "").strip()
                    pkg = pkg.replace(";", "").strip()
                    if  isContent2(pkg):
                        keep = '-keep class ' + pkg.strip() + '{*;}'
                        keep2 = '-keep class ' + pkg.strip() + '$*{*;}'
                        imports[keep]="1"
                        imports[keep2] ="1"



    filePath='./res/import.txt'

    exists2 = os.path.exists(filePath)
    if exists2:
        os.remove(filePath)
    file = open(filePath, 'a+')
    for pkg in imports.keys():
        file.write(pkg+"\n")
    print(imports)


def isContent2(name):
    cls = ["com.",

          ]
    end=['.R']

    for item in cls:
        if name.startswith(item):
            return True

    for item in end:
        if name.endswith(item):
            return False

    return False

if __name__ == '__main__':
    # writeNewMapping()
    # writeNewCls()
    # runObs()
    # readMapping()
    # readSeed()
    scanImport()
