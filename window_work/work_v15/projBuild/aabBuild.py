#coding:utf-8
import datetime
import shutil
import subprocess
import sys
import zipfile
import os
import chardet
import json
workspace_dir = "workspace"



def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))
def cmd(cmd):
    subprocess.run(cmd, shell=True)


def clean(path):
    if os.path.exists(path):
        cmd('rmdir /s /q ' + path)
        print("clean->" + path)
        # shutil.rmtree(path)

def byteToStr(output: bytes):
    encoding = chardet.detect(output)["encoding"]
    s = output.decode(encoding).encode('utf-8')
    return str(s,'utf-8')

def replaceLocalProperties(prjPath,sdkPath):
    filePath = prjPath+"/local.properties"
    newLines = []
    if  os.path.exists(filePath):
        file = open(filePath, "rb+")
        lines = file.readlines()
        for line in lines:
            l = byteToStr(line)
            if l.__contains__("sdk.dir"):
                continue
            else:
                newLines.append(l.replace('\r', ''))
        file.close()
        os.remove(filePath)  # 先删除
    newLines.append("\n")
    newLines.append("sdk.dir="+sdkPath)
    newFile = open(filePath, "w+")
    newFile.writelines(newLines)
    newFile.close()

def replaceGradleProperties(prjPath,config):
    """
    二.输入打包参数
    1. 是否白包
    2. 出包游戏编号
    3. 隐私地址
    :return:
    """
    filePath = prjPath+"/gradle.properties"
    if not os.path.exists(filePath):
        print(filePath + " not exist")
        raise Exception('1231')
    file = open(filePath, "rb+")
    lines = file.readlines()
    file.close()
    newLines = []
    for line in lines:
        l = byteToStr(line)
        if containsKey(l,config):
            continue
        else:
            newLines.append(l.replace('\r', ''))
    newLines.append("\n")
    for key in config.keys():
        newLines.append(key+'=' + str(config[key]) + "\n")

    os.remove(filePath)
    newFile = open(filePath, "wb")
    for line in newLines:
        l=line.encode('utf-8')
        newFile.write(l)
    newFile.close()

def containsKey(key,list):
    for item in list:
        if key.__contains__(item):
            return True

    return False

def down(proName, gitPath, branch, modulesBranch):
    workDir = os.getcwd() + "/" + workspace_dir
    print("workDir->" + workDir)
    if not os.path.exists(workDir):
        os.makedirs(workDir)
    os.chdir(workDir)  # 先切到工作目录
    cmd('git clone --depth=1 -b ' + branch + ' --recurse-submodules ' + gitPath)  # 正常拉取主模块以及子模块
    os.chdir(workDir + "/" + proName)  # 再切到项目目录
    print('reset dir->' + os.getcwd())

    if modulesBranch is not None:
        """
        由于主仓库浅克隆,子模块无法切换分支, 需要重新将子模块的git clone下来
        这里先把原本的modules目录删除
        """
        sp=gitPath.split("//")
        sp1=sp[0]
        sp2=sp[1].split("/")[0]
        modulesPath =sp1+"//"+sp2+'/chuangxin2/common-components/modules-archrepo.git'
        print('modulesPath->' + modulesPath)
        print(os.getcwd() + "\\modules")
        clean(os.getcwd() + "\\modules")
        cmd('git clone --depth=1 -b ' + modulesBranch +' '+modulesPath+'  modules')  # 正常拉取主模块以及子模块

        # os.chdir(os.getcwd() + "/modules")  # 再切到项目目录
        # print('reset dir->' + os.getcwd())
        # cmd('git checkout ' + modulesBranch)
        # cmd('git pull')
        # os.chdir('../')

    # 把目录重置到根目录
    os.chdir('../../')  # 再切到项目目录
    print('reset dir->' + os.getcwd())

def build(prjDirPath,isBuildApk):
    if isBuildApk == "true":
        buildType = "assembleRelease"
    else:
        buildType = "aabresguardRelease"
    # 使用 Gradle 命令打包 AAB
    os.chdir(prjDirPath)
    command = "gradlew "+buildType+" --stacktrace -x lint"
    result = subprocess.run(command, shell=True)
    os.chdir("../../")
    print(os.getcwd())
    if result.returncode != 0:
        print("Failed to build AAB")
    else:
        # 获取 AAB 文件路径
        try:
            output = projPath + "/app/build/outputs"
            if os.path.exists(output):
                # 移动 AAB 文件到指定目录
                dest_dir = os.getcwd() + "/aab"
                if not os.path.isdir(dest_dir):
                    os.makedirs(dest_dir)
                outZip = dest_dir + '/game' '_' + datetime.datetime.now().strftime('%Y%m%d%H%M') + ".zip"
                zip_folder(output, outZip)
                print("AAB saved to:", outZip)
            else:
                print("AAB file not found")
        except:
            print('except')

def getProjDirName(gitPath):
    """
    获取项目目录名称
    :return:
    """
    spArr = gitPath.split("/")
    projName = spArr[spArr.__len__() - 1].replace(".git", '')  # 项目名称
    return projName

def getConfig():
    with open("Config.txt", "r") as f:
        data = json.load(f)
    print(data)
    return data


if __name__ == '__main__':
    sdkPath=(os.getcwd().replace("projBuild",'')+"tools\\Sdk").replace("\\","\\\\").replace(":","\\:")
    config = getConfig()
    gitPath = config.get("gitPath")
    gitBranch = config.get("gitBranch")
    modulesBranch = config.get("modulesBranch")
    isClean = config.get("isCleanDir")
    isBuildApk = config.get("isBuildApk")

    if gitPath is None or gitBranch is None:
        raise Exception("参数不全")

    projDirNm = getProjDirName(gitPath)
    os.chdir('./')
    workspacePath = os.getcwd() + "\\" + workspace_dir
    projPath = workspacePath + "\\" + projDirNm
    if isClean == "false":
        print("not clean , do build")
    else:
        print('clean old workspace->' + str(workspacePath))
        clean(workspacePath)
        print(os.getcwd())
        down(projDirNm, gitPath, gitBranch, modulesBranch)  # 下载仓库

    replaceLocalProperties(projPath, sdkPath)
    replaceGradleProperties(projPath, config)
    print(os.getcwd())
    build(projPath,isBuildApk)



