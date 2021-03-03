import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import base64
import re
import time

options = webdriver.ChromeOptions()
# 一些网站能够识别selenium并进行针对性拒绝访问，这里设置options为开发者模式，防止被网站识别出来使用了Selenium
# 我实际用了几次（比如在淘宝和CSDN的登录上）已经没有效果了，应该是反爬机制又升级了
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--headless')  # 不启动浏览器操作（默认会真正启动浏览器）
driver = webdriver.Chrome(
    executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe',
    options=options
)
# 其中executable_path传入的是驱动程序的路径，需要下载，谷歌浏览器可以参见https://blog.csdn.net/weixin_43746433/article/details/95237254
# driver = webdriver.Firefox()


driver.get("http://www.jd.com")
driver.find_element_by_link_text("你好，请登录").click()  # 就是你在页面上看到的可点击元素
time.sleep(2)   # 限于网络环境需要适当延迟等网页刷新页面
driver.find_element_by_link_text("账户登录").click()
driver.find_element_by_name("loginname").send_keys('123456')   # 通过查看源码获得的html元素中的name属性
driver.find_element_by_name("nloginpwd").send_keys('mimamima')
driver.find_element_by_id("loginsubmit").click()    # # 通过查看源码获得的html元素中的name属性
time.sleep(1)

background = driver.find_element_by_id('logo').find_element_by_tag_name('img')
url = background.get_property('src')  # url被卸载了style属性中
print(url)
r = requests.get(url)
# 这里通过requests来获取这张图片，当然driver也是可以的，但是driver之后当前的dirver处理页面就变成了这张图片
# 再找元素就找不到了，转回来也会比较麻烦
with open('./data/logo.png', 'wb') as f:   # 注意文件处理模式为‘wb’（以二进制写入）
    f.write(r.content)  # r.content获取r的二进制形式



img = driver.find_element_by_class_name('JDJRV-bigimg').find_element_by_tag_name('img')
src = img.get_attribute('src')
b64 = src.split(',')[-1]    # 从src内容中拆解出图片的base64码
imgdata = base64.b64decode(b64)
file = open('data/verify.png', 'wb')
file.write(imgdata)
file.close()


# soup = BeautifulSoup(driver.page_source, 'lxml')
# imgs = soup.find('div', {'class': 'JDJRV-img-wrap'}).find_all('img')
# # 找到底图和滑块图所在的html元素
# srcs = [im.attrs.get('src') for im in imgs] # 获取src属性
# b64s = [src.split(',')[-1] for src in srcs]
# # 这里的图片是以base64直接出现在html源码中的，从src中提取图片的base64码
# save_path = ['data/big.png', 'data/small.png']
# for i in range(2):
#     imgdata = base64.b64decode(b64s[i])
#     file = open(save_path[i], 'wb')
#     file.write(imgdata)
#     file.close()


