import pyaudio
import numpy as np
import pyautogui
import time

# 需要 安装虚拟音频设备 https://vb-audio.com/Cable/

# 定义音频参数
FORMAT = pyaudio.paInt16  # 16位格式
CHANNELS = 2  # 立体声
RATE = 44100  # 采样率
CHUNK = 10240*10  # 块大小

# 初始化pyaudio
audio = pyaudio.PyAudio()

# 获取系统中的音频设备信息
info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

# 列出所有的输入设备
for i in range(0, numdevices):
    if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print(f"Input Device id {i} - {audio.get_device_info_by_host_api_device_index(0, i).get('name')}")

# 替换为你的虚拟音频设备的 ID
input_device_index = int(input("Enter the input device ID to use: "))

# 打开流
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=input_device_index,
                    frames_per_buffer=CHUNK)

print("开始监听音频输出...")


def detect_sound(data, threshold=1000):
    """ 检测音频数据中是否有超过阈值的声音 """
    audio_data = np.frombuffer(data, dtype=np.int16)
    peak = np.abs(audio_data).max()
    if peak >= threshold:
        print("当前声音阀值:" + str(peak))
        return True
    return False


try:
    while True:
        data = stream.read(CHUNK)
        if detect_sound(data,1000):  # 填写声音阈值
            print("检测到声音，按键 '1' 被点击")
            # 等待1秒，以防止连续触发
            # time.sleep(7)

        time.sleep(0.2)
except KeyboardInterrupt:
    print("停止监听")
finally:
    # 停止并关闭流
    stream.stop_stream()
    stream.close()
    audio.terminate()
