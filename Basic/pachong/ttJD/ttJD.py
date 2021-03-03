import base64
import datetime
import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from Basic.pachong.ttJD.Easing import *
import numpy as np
import time

class OptJD:
    def __init__(self, username='username', password='password'):
        self.uname = username
        self.upwd = password

        self.driver = webdriver.Chrome(
            executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
        self.url_login = 'https://passport.jd.com/new/login.aspx'

    def login(self):
        self.driver.get(self.url_login)
        self.driver.find_element_by_link_text("账户登录").click()
        self.driver.find_element_by_name("loginname").send_keys(self.uname)
        self.driver.find_element_by_name("nloginpwd").send_keys(self.upwd)
        self.driver.find_element_by_id("loginsubmit").click()
        while True:
            # 获取滑块图片的cv2对象
            big, small = self.get_slider_imgs()
            offset = self.get_distance(big, small)
            track = self.get_track(offset, 1)
            success = self.move_to_gap(track)
            if success:
                break
        time.sleep(3)

    def get_slider_imgs(self):
        '''
        获取滑块验证的图片，包括带缺口背景图和缺口填充图
        :return: 返回两个图片的cv2对象
        '''
        # 将网页源码转化为能被解析的lxml格式
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        imgs = soup.find('div', {'class': 'JDJRV-img-wrap'}).find_all('img')
        srcs = [im.attrs.get('src') for im in imgs]
        b64s = [src.split(',')[-1] for src in srcs]  # 图片是以base64直接出现在html源码中的
        # 转成cv2对象
        res = []
        for cell in b64s:
            imgString = base64.b64decode(cell)
            nparr = np.fromstring(imgString, np.uint8)
            res.append(cv2.imdecode(nparr, cv2.IMREAD_COLOR))
        return res

    def get_distance(self, bg, cell):
        '''
        计算滑动距离（JD的滑块横轴起始位置为0，只要找到缺口的位置即为滑动距离）
        :param bg: 带缺口背景图
        :param cell: 填充小块
        :return:
        '''
        # 非主要矛盾，未做研究,解释可见参考文献
        res = cv2.matchTemplate(bg, cell, cv2.TM_CCOEFF_NORMED)
        value = cv2.minMaxLoc(res)
        # (-0.5858383774757385, 0.38912370800971985, (85, 71), (45, 72))
        key = value[2] if abs(value[0]) > abs(value[1]) else value[3]
        return int(key[0] * 278 / 360)  # 278登录页面显示长度，360实际长度

    def get_track(self, distance, seconds):
        tracks = [0]
        offsets = [0]
        for t in np.arange(0.0, seconds, 0.1):
            offset = round((1 - (1 - t / seconds)**2)  * distance)
            tracks.append(offset - offsets[-1])
            offsets.append(offset)
        # return offsets, tracks
        return tracks

    def move_to_gap(self, track):
        # 得到滑块标签
        slider = self.driver.find_element_by_class_name('JDJRV-slide-btn')
        # 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
        ActionChains(self.driver).click_and_hold(slider).perform()
        for x in track:
            # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        # 模拟人类对准时间
        time.sleep(1)
        # 释放滑块
        ActionChains(self.driver).release().perform()
        time.sleep(2)
        try:
            car = self.driver.find_element_by_link_text('我的购物车')
            return True  # 如果上面顺利找到了，说明登录成功
        except:
            return False

    def to_car(self):
        # nowwhandle = self.driver.current_window_handle  # 获取当前窗口
        self.driver.find_element_by_link_text('我的购物车').click()  # 购物车会新打开一个页面
        # allhandles = self.driver.window_handles     # 获取所有窗口
        # for handle in allhandles:
        #     if handle != nowwhandle:    # 新开的浏览器，除了刚才登陆操作的那一个，就是购物车的这一个
        #         self.driver.switch_to.window(handle)  # 切换至窗口 购物车页面
        self.driver.get("https://cart.jd.com/cart.action")  # # 切换至窗口 购物车页面
        self.driver.find_element_by_link_text('去结算').click()
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

    def buy_on_time(self, buytime):
        buytime = time.mktime(time.strptime(buytime, "%Y-%m-%d %H:%M:%S"))
        while True:
            if time.time()>=buytime:
                if time.time()-buytime>30: # 30s后退出
                    print('may be false...')
                    break
                try:
                    try:
                        # print(time.time(), 'find 支付')
                        self.driver.find_element_by_link_text('立即支付')
                        print('may be success~')
                        break
                    except:
                        pass
                    # print(time.time(), 'find 提交')
                    self.driver.find_element_by_id('order-submit').click()  # 提交订单
                except:
                    # time.sleep(0.1)
                    pass

            time.sleep(0.5)

def dosomething():
    obj = OptJD(username='uname', password='pwd')
    obj.login()
    obj.to_car()
    obj.buy_on_time('2020-03-17 12:54:00')

if __name__ == '__main__':
    dosomething()

# 使用说明
# 先别动程序，一面坏了下面几行的索引
# 17行：这是一个谷歌浏览器的驱动，路径指定为驱动物理地址
# 133行：设置用户名和密码
# 136行：抢购的时间点
# 准备工作：要抢的商品加入购物车；设置到选中状态；这个程序就夸夸的点 提交订单 按钮
# 提前运行程序，处于登陆状态等着，因为登陆那块不能保证100%一次成功