# coding=gbk
import os
import sys
os.system('chcp 65001')
sys.path.insert(0, r'C:\Program Files\SDK\platform-tools')  # 这个也不成
# 最终把3个adb的文件考到了sys.path的envs/others目录下

import time

# cmd = 'adb version'
# cmd = 'adb shell dumpsys window displays' # 获取屏幕信息
# 'adb shell wm size'
# 'adb shell input touchscreen swipe 1200 1000 600 1000'  # 滑动,坐标好像是左上角原点，向右，向下
cmd = '''
    adb shell input keyevent 3 & \
    adb shell input swipe 1200 1000 600 1000 & \
    adb shell input tap 100 300 & \
    adb devices
'''
# os.system(cmd)
# time.sleep(5)
cmd2 = '''
    adb shell input tap 200 2000 & \
'''
# os.system(cmd2)
for i in range(1000):
    print(i)
    os.system('adb shell wm size')
    os.system('adb shell input tap 1500 80')
    time.sleep(2)
    # os.system('adb shell input tap 800 830')
    os.system('adb shell input tap 800 1280')
    time.sleep(35)
    os.system('adb shell input tap 1530 70')
    # os.system('adb shell input tap 70 70')
# os.system('adb shell input tap 1580 2540')
# os.system('adb shell input swipe 1200 1000 600 1000')



# os.system('adb devices')
# os.system('ipconfig')
# print(sys.path)
# print(os.environ)

print('over')
