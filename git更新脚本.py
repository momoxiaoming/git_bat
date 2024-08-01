# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

GIT_PATH = "D:\zhangjinming\work\git"  # 本地git项目目录

# 所有本地项目
PROJECT_LIST = [
    # {"name": "AnswerMakeMoney", "app": "develop", "ng": "develop", "modules": "develop", "biz": "develop","game": "develop"},
    # {"name": "viWeather", "app": "develop", "ng": "develop", "modules": "develop", "biz": "develop","game": "develop"},
    # {"name": "hugefontyi", "app": "develop", "ng": "develop", "modules": "develop", "biz": "develop","game": "develop"},
    # {"name": "RedPacketGroup", "app": "develop", "ng": "develop", "modules": "develop", "biz": "develop","game": "develop"},
    # {"name": "GroupApp", "app": "develop", "ng": "develop", "modules": "develop", "biz": "develop","game": "develop"},
    # {"name": "Calendar", "app": "develop", "ng": "develop", "modules": "develop", "biz": "develop", "game": "develop"},
    # {"name": "runningman", "app": "master", "ng": "develop", "modules": "develop", "biz": "develop", "game": "develop"},
    {"name": "GroupApp2\\GroupApp", "app": "release", "ng": "release", "modules": "release", "biz": "release", "game": "release"},

]


def listAllPath():
    """
    列出所有本地git项目
    :return:
    """
    files = os.listdir(GIT_PATH)  # 得到文件夹下的所有文件名称

    for project in PROJECT_LIST:
            updateProject(project)



def updateProject(project):
    """
    更新每个项目中的git
    :param name:
    :return:
    """
    path = GIT_PATH + "\\" + project["name"]
    filePath = os.path.join(path)

    if os.path.isdir(filePath):
        os.chdir(filePath)  # 移动到指定目录下
        updateAllSub(filePath, project)
        os.chdir(filePath)  # 移动到指定目录下
        updateMain(project)


def updateMain(project):
    """
    更新主模块
    :param project:
    :return:
    """
    cmd("git pull")
    cmd("git add .")
    cmd("git commit -m 'update'")
    cmd("git push origin "+project["app"])


def updateAllSub(path, project):
    """
    更新所有子模块
    :param path:
    :return:
    """
    updateSubmodule(path + "\\" + "app", project["app"])
    updateSubmodule(path + "\\" + "modules", project["modules"])
    updateSubmodule(path + "\\" + "biz", project["biz"])
    updateSubmodule(path + "\\" + "ng", project["ng"])
    updateSubmodule(path + "\\" + "game", project["game"])


def updateSubmodule(path, branch):
    """
    更新子模块
    :return:
    """
    print("子模块更新开始-path->" + path)
    os.chdir(path)  # 移动到指定目录下
    b = cmd("git branch")
    for sp in b.split("\n"):
        if sp.__contains__("*"):
            local_branch = sp.split(" ")[1]
            temp = True
            if branch != local_branch:
                b = cmd("git checkout " + branch)  # 切换到我们指定分支
                temp = b.__contains__("Switched to branch")
                print("分支" + branch + "切换成功")
            if temp:
                cmd("git pull ")
                print("分支" + branch + "更完毕")
                # 分支正确,拉取最新内容


def cmd(cmd):
    b = os.popen(cmd).read()
    if b.__contains__("error"):
        raise RuntimeError('命令出错,中断运行')
    return b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listAllPath()
