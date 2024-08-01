# -*- encoding=utf8 -*-
import os
from datetime import time
from time import sleep
import time
import requests
from bs4 import BeautifulSoup

def findNodeForId(soup, clsStr):
    return soup.find_all(id_=clsStr)

def findNodeForId(soup, clsStr):
    return soup.find_all(id_=clsStr)

def findNodeForClass(soup, clsStr):
    return soup.find_all(class_=clsStr)


if __name__ == '__main__':
    soup = BeautifulSoup("", "html.parser")
    findNodeForClass(soup, 'test')
