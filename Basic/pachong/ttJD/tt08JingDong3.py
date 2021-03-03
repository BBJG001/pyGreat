# Python3.5

# coding:utf-8

# import scrapy

from selenium import webdriver
import time
import datetime
driver = webdriver.Firefox()
driver.get('https:www.jd.com/')

class JDLOGIN(object):

    def login_jd(self, num, pwd):
        driver.find_element_by_link_text('你好，请登录').click()
        time.sleep(10)
        driver.find_element_by_link_text('账户登录').click()
        time.sleep(3)
        driver.find_element_by_id('loginname').send_keys(num)
        driver.find_element_by_id('nloginpwd').send_keys(pwd)
        time.sleep(3)
        driver.find_element_by_id('loginsubmit').click()
        time.sleep(5)
        nowwhandle = driver.current_window_handle
        driver.find_element_by_link_text('我的购物车').click()
        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != nowwhandle:
                driver.switch_to_window(handle)  # 切换至窗口 购物车页面
        time.sleep(5)
        driver.find_element_by_link_text('去结算').click()
        time.sleep(4)

    def buy_on_time(self, buytime):

        while True:
            now = datetime.datetime.now()
            if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
                driver.find_element_by_id('order-submit').click()
                time.sleep(3)
                print(now.strftime('%Y-%m-%d %H:%M:%S'))
                print('successful!!!')
            time.sleep(0.5)
            # 返回原先到的窗口
            # driver.switch_to_window(nowwhandle)

    def start(self, num, pwd, buytime):
        self.login_jd(num, pwd)
        self.buy_on_time(buytime)


jdlogin = JDLOGIN()
jdlogin.start('手机号', '密码', '秒杀时间')
