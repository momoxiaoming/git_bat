# -*- encoding=utf8 -*-
import os
from datetime import time
from time import sleep
import time
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",

}


def down_video(url,category):
    try:
        file_path = './video/'+category
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_name = str(int(round(time.time() * 1000))) + '.mp4'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(file_path + "/" + file_name, 'wb') as file:
                file.write(response.content)
            print('video downloaded successfully')
        else:
            print('Failed to download video ,' + str(response.status_code))
    except Exception as e:
        print("download_video error")
        print(e)


def getVideoDownUrl(url,category):
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, "html.parser")
    topmenu = soup.find_all(class_='wpdm-download-link')
    if len(topmenu) > 0:
        downUrl = topmenu[1].get('data-downloadurl')
        print("下载地址->" + str(downUrl))
        down_video(downUrl,category)


def getVideoInfoList(url,page,category):
    """
    获取视频信息
    :return:
    """
    try:
        url = url + 'page/' + str(page)
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, "html.parser")
        topmenu = soup.find_all(id='posts')
        a = topmenu[0].find_all(class_='category-mobile-resolution')
        for i in a:
            href = i.get('href')
            sleep(1)
            getVideoDownUrl(href,category)
    except Exception as e:
        print('getVideoInfoList error')


def downVideoWallpage(url,page,category):
    for i in range(1, page):
        getVideoInfoList(url,i,category)
        sleep(1)


def getCategory():
    data = requests.get('https://mylivewallpapers.com/', headers=headers)
    soup = BeautifulSoup(data.text, "html.parser")
    sp = soup.find(class_='menu-item-726')
    category = sp.find_all(class_='menu-item-object-category')
    list = []
    for item in category:
        a = item.find(name='a')
        href=a.get('href')
        cgy=a.string
        list.append({'url':href,'category':cgy})

    print(list)
    return list


if __name__ == '__main__':
    list = getCategory()
    for item in list:
        url=item['url']
        category=item['category']
        downVideoWallpage(url,20,category)  ##默认只拿20页,想拿多少自己改

