import pygetwindow as gw
import pyautogui
import threading
import time

import win32api
import win32con
import win32gui
from pywinauto import application

from pywinauto import application


def send_input_without_focus(window_title, text_to_type):
    # 启动应用程序（这里假设程序已经在运行，因此我们附加到它）
    app = application.Application().connect(title=window_title)

    # 获取窗口句柄
    # window = app.window(title=window_title)

    # 发送输入到窗口
    # window.type_keys(1)


if __name__ == "__main__":
    send_input_without_focus('1.txt - Notepad', 'Hello, World!')