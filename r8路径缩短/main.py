import os
import shutil

def clear_folder_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def list_folder_files(folder_path):
    list=[]
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            list.append(file_path)
    return list

def copy_file(source_file, destination_file):
    with open(source_file, 'rb') as f_source:
        with open(destination_file, 'wb') as f_dest:
            for line in f_source:
                f_dest.write(line)

so_obs_path="D:\\so_obs\\"

if __name__ == '__main__':
    # 读取lib_config文件,把里面内容转文件复制到aar目录下
    data = open("./lib_config")
    content = data.read()
    list = content.split("--lib")
    index = 0
    clear_folder_files(so_obs_path)
    for i in list:
        item = i.replace(" ", "").replace("\\","\\\\")
        print(item)
        if os.path.exists(item):
            copy_file(item,so_obs_path + str(index) + ".jar")
            index = index + 1

    list=list_folder_files(so_obs_path)
    lib_config=""
    for i in list:
        lib_config=lib_config+" --lib "+i


    print(lib_config)

