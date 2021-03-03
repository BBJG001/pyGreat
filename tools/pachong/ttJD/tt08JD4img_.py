import base64

import cv2
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import time

# 初始化
def init():
    # 定义为全局变量，方便其他模块使用
    global url, browser, username, password, wait, bgp, sliderp
    # 登录界面的url
    # url = 'https://passport.bilibili.com/login'
    url = 'https://passport.jd.com'
    # url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
    # url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https://www.jd.com/'
    # url = 'https://passport.jd.com/new/login.aspx'
    # 实例化一个chrome浏览器
    # browser = webdriver.Chrome()    # driver
    browser = webdriver.Chrome(
        executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
    # 用户名
    username = '17852847713'
    # 密码
    password = 'z19950513y'
    # 设置等待超时
    wait = WebDriverWait(browser, 20)

    bgp = 'data/big.png'

    sliderp = 'data/small.png'


def login():
    browser.get("http://www.jd.com")
    browser.find_element_by_link_text("你好，请登录").click()
    time.sleep(1)
    browser.find_element_by_link_text("账户登录").click()
    browser.find_element_by_name("loginname").send_keys(username)
    browser.find_element_by_name("nloginpwd").send_keys(password)
    browser.find_element_by_id("loginsubmit").click()


# 获取图片信息
def get_images(bp, sp):
    '''
      :param img: (Str)想要获取的图片类型：带缺口、原始
      :return: 该图片(Image对象)、位置信息(List)
    '''
    # 将网页源码转化为能被解析的lxml格式
    soup = BeautifulSoup(browser.page_source, 'lxml')
    # 获取验证图片的所有组成片标签
    # < div class ="JDJRV-bigimg" style="height: 108.111px;" > < img src="data:image/png;base64,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" > < / div >
    imgs = soup.find('div', {'class': 'JDJRV-img-wrap'}).find_all('img')
    srcs = [im.attrs.get('src') for im in imgs]
    b64s = [src.split(',')[-1] for src in srcs]
    path = [bp, sp]
    for i in range(2):
        imgdata = base64.b64decode(b64s[i])
        file = open(path[i], 'wb')
        file.write(imgdata)
        file.close()


# 计算滑块移动距离
def get_distance(target, template):
    """
    找出图像中最佳匹配位置
    :param target: 目标即背景图
    :param template: 模板即需要找到的图
    :return: 返回最佳匹配及其最差匹配和对应的坐标
    因为京东的滑块每次都在最左侧，所以找到缺口的位置提取横坐标即为移动距离
    """
    target_rgb = cv2.imread(target)
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    template_rgb = cv2.imread(template, 0)
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)
    # (-0.5858383774757385, 0.38912370800971985, (85, 71), (45, 72))
    key = value[2] if abs(value[0]) > abs(value[1]) else value[3]
    return key[0]


# 构造滑动轨迹
def get_track2(distance):
    '''
  :param distance: (Int)缺口离滑块的距离
  :return: (List)移动轨迹
  '''

    # 创建存放轨迹信息的列表f
    trace = []
    # 设置加速的距离
    faster_distance = distance * (3 / 4)
    # 设置初始位置、初始速度、时间间隔
    start, v0, t = 0, 0, 0.5
    # 当尚未移动到终点时
    while start < distance:
        # 如果处于加速阶段
        if start < faster_distance:
            # 设置加速度为2
            a = 10
        # 如果处于减速阶段
        else:
            # 设置加速度为-3
            a = -20
        # 移动的距离公式
        move = v0 * t + 1 / 2 * a * t * t
        # 此刻速度
        v = v0 + a * t
        # 重置初速度
        v0 = v
        # 重置起点
        start += move
        # 将移动的距离加入轨迹列表
        trace.append(round(move))
    # 返回轨迹信息
    return trace


def get_track3(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.3
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track

# 模拟拖动
def move_to_gap(trace):
    # 得到滑块标签

    slider = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'JDJRV-slide-btn')))

    # slider = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'JDJRV-slide-btn')))

    # iframe = browser.find_element_by_xpath('//iframe')  # 找到“嵌套”的iframe
    # browser.switch_to.frame(iframe)  # 切换到iframe
    # slider = browser.find_element_by_class_name('JDJRV-slide-btn')

    # 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
    ActionChains(browser).click_and_hold(slider).perform()
    for x in trace:
        # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
    # 模拟人类对准时间
    time.sleep(1)
    # 释放滑块
    ActionChains(browser).release().perform()
    time.sleep(2)
    try:
        test = browser.find_element_by_link_text('我的购物车')
        return True    # 如果上面顺利找到了，说明登录成功
    except:
        return False

# 主程序
def main():
    # 初始化
    init()
    # 登录
    login()

    while True:
        time.sleep(1)
        # 获取图片
        get_images(bgp, sliderp)
        # 算法识别获取缺口距离
        distance = get_distance(bgp, sliderp)
        # 显示尺寸与实际尺寸不符！！！
        distance = int(distance*278/360)
        # 计算移动轨迹
        trace = get_track(distance, 1)
        # 移动滑块
        success = move_to_gap(trace)
        if success:
            break


    time.sleep(5)


# 程序入口
if __name__ == '__main__':
    main()
