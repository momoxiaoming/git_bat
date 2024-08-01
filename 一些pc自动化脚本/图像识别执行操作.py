import pyautogui
import time
import pyautogui

targetImg = "./file/screenshot-20240801-110548.png"


def doThings():
    i = 1


def listener():
    screen_width, screen_height = pyautogui.size()
    region = (0, 0, screen_width, 600)
    while True:
        pyautogui.screenshot("./file/shot.png",region=region)
        if pyautogui.locateCenterOnScreen(targetImg) is not None:
            print("图像已匹配")
            doThings()
        else:
            print("图像未匹配")
        time.sleep(0.2)  # 1s截取一张


if __name__ == '__main__':
    listener()
