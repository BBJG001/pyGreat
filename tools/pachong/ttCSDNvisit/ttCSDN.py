# 失败
# selenium被限制，在淘宝上表现尤为多
# 开发者模式下也不起作用，开发者模式下手动登录也不行
import base64
import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import time


class OptCSDN:
    def __init__(self, username, password):
        self.uname = username
        self.upwd = password

        # 失败
        # https://www.imooc.com/article/285729?block_id=tuijian_wz
        # options = webdriver.ChromeOptions()
        # # 此步骤很重要，设置为开发者模式，防止被网站识别出来使用了Selenium
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.dirver = webdriver.Chrome(
            executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe',
            # options=options
        )
        self.url_login = 'https://passport.csdn.net/login'


    def login(self):
        self.dirver.get(self.url_login)
        self.dirver.find_element_by_link_text("账号密码登录").click()
        self.dirver.find_element_by_name("all").send_keys(self.uname)
        self.dirver.find_element_by_name("pwd").send_keys(self.upwd)
        self.dirver.find_element_by_class_name("btn-primary").click()
        while True:
            time.sleep(10)
            try:
                slider = self.dirver.find_element_by_id('nc_1_n1z')
                self.move_slider(slider)
            except:
                break
        # while True:
        #     # 获取滑块图片的cv2对象
        #     big, small = self.get_slider_imgs()
        #     offset = self.get_distance(big, small)
        #     track = self.get_track(offset, 1)
        #     success = self.move_to_gap(track)
        #     if success:
        #         break
        time.sleep(3)

    def get_slider_imgs(self):
        '''
        获取滑块验证的图片，包括带缺口背景图和缺口填充图
        :return: 返回两个图片的cv2对象
        '''
        # 将网页源码转化为能被解析的lxml格式
        soup = BeautifulSoup(self.dirver.page_source, 'lxml')
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
        slider = self.dirver.find_element_by_class_name('JDJRV-slide-btn')
        # 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
        ActionChains(self.dirver).click_and_hold(slider).perform()
        for x in track:
            # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
            ActionChains(self.dirver).move_by_offset(xoffset=x, yoffset=0).perform()
        # 模拟人类对准时间
        time.sleep(1)
        # 释放滑块
        ActionChains(self.dirver).release().perform()
        time.sleep(2)
        try:
            car = self.dirver.find_element_by_link_text('我的购物车')
            return True  # 如果上面顺利找到了，说明登录成功
        except:
            return False

    def move_slider(self, slider):
        # 得到滑块标签
        # slider = self.dirver.find_element_by_id('nc_1_n1z')
        # 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
        ActionChains(self.dirver).click_and_hold(slider).perform()
        # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
        track = [26]*10
        # track = [260]
        for x in track:
            # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
            ActionChains(self.dirver).move_by_offset(xoffset=x, yoffset=0).perform()
        # 释放滑块
        ActionChains(self.dirver).release().perform()
        time.sleep(2)
        try:
            car = self.dirver.find_element_by_link_text('我的购物车')
            return True  # 如果上面顺利找到了，说明登录成功
        except:
            return False

if __name__ == '__main__':
    uname = 'BBJG_001'
    upwd = 'asd123456789'

    obj = OptCSDN(uname, upwd)
    obj.login()
