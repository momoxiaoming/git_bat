# coding:utf-8
import os, sys
import subprocess



def cmd(cmd):
    subprocess.run(cmd, shell=True)

def mergedDex(dexPath,outputPath):
    """
    使用android sdk 自带的dx工具
    dx --dex --output=merged_dex.dex dex_file1.dex dex_file2.dex dex_file3.dex ...
    :param dexPath:
    :param outputPath:
    :return:
    """
    #
    files=os.listdir(dexPath)
    # dex=""
    for file in files:
        sh= "jadx -j 1 -r -d "+outputPath+" "+file.
    output=outputPath+"/merged_dex.dex"
    cmdstr="dx --dex --output= "+output+" "+dexPath+"/*.dex"
    print(cmdstr)
    print(cmd(cmdstr))


if __name__ == '__main__':
    os.chdir("./")
    print(os.getcwd())
    mergedDex(os.getcwd()+'/dex',os.getcwd())