import subprocess
import sys
import time

import frida

from pip._vendor.distlib.compat import raw_input


def cmd(cmd):
    subprocess.run(cmd, shell=True)

def my_message_handler(message , payload): #定义错误处理
	print(message)
	print(payload)

if __name__ == '__main__':
    # cmd('adb shell "su -c /data/local/tmp/frida-server-15.2.2-android-arm64 &"')  #开启手机端frida-server

    pkg='colorf.wall.canvas.hushg'  #hook的包名

    device = frida.get_usb_device()
    pid = device.spawn(pkg)
    print("pid-->" + str(pid))
    device.resume(pid)
    print("resume")
    # time.sleep(1)
    session = device.attach(pid)
    print("attach")
    with open('script/testApk2.js', 'r', encoding='utf-8') as file:
        script_code = file.read()

    script = session.create_script(script_code)
    script.on("message", my_message_handler)  # 调用错误处理
    script.load()
    # 脚本会持续运行等待输入
    raw_input()
