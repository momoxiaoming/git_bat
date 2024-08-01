# -*- encoding=utf8 -*-
import os
from datetime import time
from time import sleep

import requests
from bs4 import BeautifulSoup


def getClassContent():
    """
    获取分类数据
    :return:
    """
    url = 'https://wallhaven.cc/latest'
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    topmenu = soup.find_all(class_='topmenu-primary')
    a = topmenu[0].find_all(name='a')
    list = []
    for i in a:
        span = i.find_all('span')[0]
        type = span.string
        href = i.get('href')
        if type == 'Upload':
            # 此分类后为无效分类
            break
        else:
            list.append({"type": type, "url": href})

    print(list)

    new_list = getPageNum(list)
    print(new_list)
    return new_list


def getPageNum(list):
    new_list = []
    for item in list:
        url = item['url']
        print("req->" + url)
        soup1 = BeautifulSoup(requests.get(url).text, "html.parser")
        pagination = soup1.find_all(class_='pagination')[0]
        page_html = pagination.find_all(name='a')
        page = page_html[len(page_html) - 2].string
        item['page'] = page
        new_list.append(item)

    return new_list


def getPicForPage2(url, type):
    """
    获取分页图片信息地址
    :return:
    """
    try:
        print(url)
        data = requests.get(url)
        soup = BeautifulSoup(data.text, "html.parser")
        thumb_list = soup.find_all(class_='thumb-listing-page')[0]
        preview = thumb_list.find_all(class_='preview')
        print(preview)
        for item in preview:
            href = item.get('href')
            print(href)
            pic_url = getPicUrl(href)
            if pic_url is None:
                continue
            print("下载-->" + str(pic_url))
            sleep(1)
            download_image(pic_url, type)
    except Exception as e:
        print("getPicForPage error")
        print(e)


def getPicUrl(url):
    """
    通过图片信息地址拿到图片地址
    :param url:
    :return:
    """
    try:
        data = requests.get(url)
        soup = BeautifulSoup(data.text, "html.parser")
        scrollbox_html = soup.find_all(class_='scrollbox')[0]
        img_html = scrollbox_html.find_all(name='img')[0]
        pic_url = img_html.get('src')
        return pic_url
    except Exception as e:
        print(e)
    return None


def download_image(url, type):
    """
    下载图片
    :param url:
    :param file_path:
    :return:
    """
    try:
        file_path = 'pic/' + type
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        aar = str(url).split('/')
        file_name = aar[len(aar) - 1]
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path + "/" + file_name, 'wb') as file:
                file.write(response.content)
            print('Image downloaded successfully')
        else:
            print('Failed to download image')
    except Exception as e:
        print("download_image error")
        print(e)


def getCategories():
    """
    根据分类获取数据
    :return:
    """
    # classList = getClassContent()
    # print(classList)
    # 为了节省时间,直接将上面代码的抓取分类数据拿来用
    classList = [{'type': 'Random', 'url': 'https://wallhaven.cc/random', 'page': '18648'}]
    for item in classList:
        type = item['type']
        url = item['url']
        page = item['page']
        # if int(page)>100: #1页50张, 暂时只下载15页
        #     page=100
        for i in range(22, int(page)):  # 20页开始
            getPicForPage2(url + '?page=' + str(i), type)


def getSearchUrl(key, page):
    """
    根据搜索关键字,返回地址
    :param key:
    :return:
    """
    return "https://wallhaven.cc/search?q=" + key + "&categories=110&purity=100&sorting=relevance&order=desc&ai_art_filter=1&page=" + str(
        page)


def getSearchContent(key):
    """
    获取搜索的壁纸内容
    :return:
    """
    maxPage = 50  # 默认只取前50页
    for page in range(1, maxPage):
        url = getSearchUrl(key, page)
        getPicForPage2(url, key)


def getDataForSearch():
    """
    根据搜索内容获取数据
    :return:
    """
    keys = ["AI", "Babies", "Sports", "Vehicles", "Cartoon", "Halloween", "Vector", "Tourism", "Neon & Firework(美)",
            "3D", "Animal", "Super Hero(美)", "Mask(美)", "Nature", "Game", "Kawaii", "Reflections", "Alone"]
    for key in keys:
        getSearchContent(key)


if __name__ == '__main__':
    # 根据分类下载
    # getCategories()
    # 根据搜索key下载
    getDataForSearch()
