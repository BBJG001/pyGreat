import cv2
from PIL import Image
import numpy as np

# 判断像素是否相同
from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
#
# driver.get("http://www.jd.com")
# driver.find_element_by_class_name()

def FindPic(target, template):
    """
    找出图像中最佳匹配位置
    :param target: 目标即背景图
    :param template: 模板即需要找到的图
    :return: 返回最佳匹配及其最差匹配和对应的坐标
    """
    target_rgb = cv2.imread(target)
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    template_rgb = cv2.imread(template, 0)
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)
    # (-0.5858383774757385, 0.38912370800971985, (85, 71), (45, 72))
    key = value[2] if abs(value[0]) > abs(value[1]) else value[3]
    return key[0]


if __name__ == '__main__':
    # bigp = 'data/big.png'
    # smallp = 'data/small.png'
    # r = FindPic(bigp, smallp)
    # print(r)

    # browser = webdriver.Chrome(
    #     executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')

    # res = browser.find_element_by_class_name()



    big= Image.open('data/big.png')
    size_loc = big.size
    print(size_loc)
    small = Image.open('data/small.png')
    size_small = small.size
    print(size_small)