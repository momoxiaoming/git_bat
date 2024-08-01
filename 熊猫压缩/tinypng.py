import fnmatch
import os
import sys
import time

import tinify

max_limit = 500


def compressingImage(key, path):
    """
    压缩图片
    :param path:
    :return:
    """
    tinify.key = key
    # 上传本地图像
    source = tinify.from_file(path)
    # 调整图像大小
    source.to_file(path)
    print('压缩成功->' + path)


def checkKey(key, size):
    """
    检查api key是否可用
    :return:
    """

    try:
        tinify.key = key
        tinify.validate()
        count = tinify.compression_count
        return (500 - count) > size
    except tinify.AccountError as e:
        return False
    except Exception as e:
        return False


def findAllPngFiles(dirPath):
    """
    获取所有需要压缩的图片
    :return:
    """
    png_files = []
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            file_path = os.path.join(root, file)
            if fnmatch.fnmatch(file, '*.png') or fnmatch.fnmatch(file, '*.jpg') or fnmatch.fnmatch(file,
                                                                                                   '*.webp') or fnmatch.fnmatch(
                    file, '*.jpeg'):
                file_size = os.path.getsize(file_path)
                if file_size >= 100 * 1024:  # 过滤掉小于100kb的图片
                    obj = {"size": file_size, 'path': file_path}
                    png_files.append(obj)

    return png_files


def bytes_to_megabytes(bytes):
    megabytes = bytes / (1024 * 1024)
    megabytes = round(megabytes, 2)  # 保留两位小数
    return megabytes


if __name__ == '__main__':

    args = sys.argv[1:]
    if len(args) <= 0:
        raise Exception('请输入要压缩的游戏模块名')

    module_name = args[0]
    path = './' + module_name + '/src/main/assets'
    print('压缩任务开始,过程可能耗时数分钟,请耐心等待')
    time1 = int(time.time())
    files = findAllPngFiles(path)

    keys = ['p6p1b2ghcjrn3j78k0jy34qjf5avah00', 'XG77bl02kfbDQly63MPFrxWNj3CFfsyZ', 'lDfzNCrMCjqLBcbrLdtHHpw41JQVl3TF']
    # 找出一个有用的key
    apiKey = None
    for key in keys:
        if checkKey(key, len(files)):
            print('api key 可用:' + key)
            apiKey = key
            break
    if apiKey is None:
        raise Exception('无有效apikey或压缩次数不足, 无法完成压缩任务')
    old_file_size = 0
    new_file_size = 0
    for file in files:
        path = file['path']
        size = file['size']
        old_file_size += size
        compressingImage(apiKey, path)
        new_file_size += os.path.getsize(path)

    old_file_mb = bytes_to_megabytes(old_file_size)
    new_file_mb = bytes_to_megabytes(new_file_size)

    timeEnd = int(time.time()) - time1
    print('压缩任务完成!!!')
    print('过程耗时: ' + str(timeEnd) + ' 秒')
    print('压缩数量: ' + str(len(files)))
    print('压缩比例: ' + str(old_file_mb) + 'MB --> ' + str(new_file_mb) + 'MB')
