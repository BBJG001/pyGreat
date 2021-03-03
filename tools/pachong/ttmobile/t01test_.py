# 将某用户的CSDN所有博客访问一遍
# 在testvisit基础上的改进，统一获得urls列表，再进行访问
import requests
from selenium import webdriver
from bs4 import BeautifulSoup  # 解析html网页的
import re

if __name__ == '__main__':
    url = 'https://www.nunuyy.com/dongman/33730.html'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe',
        options=options
    )
    # driver.get(url)

    # driver.find_element_by_link_text('35资源').click()

    res = requests.get(url)
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.find('dl'))
    # print(soup)
    source = soup.find_all('dl')
    print(source)
    # for i in source.children:
    #     print(i)
    # print(source.children)
    article = soup.find('article')
    print(article.attrs.get('class'))
    print(article)
    video = soup.find('video')
    match = re.search(r'<video id="video" controls preload autoplay(.+)\n', res.text, flags=re.M)
    print('test0:', match.group(1))
    match = re.search(r'video id="video".*src="(\S+)"', res.text, flags=re.M)
    # < video
    # id = "video"
    # controls = ""
    # preload = ""
    # autoplay = ""
    # src = "blob:https://www.nunuyy.com/8445e0da-88b4-4616-b99a-c474e7126208" > < / video >

    # < video
    # id = "video"
    # controls = ""
    # preload = ""
    # autoplay = ""
    # src = "blob:https://www.nunuyy.com/d0aa1e79-7fff-426c-bfd7-b7ab29acaffd" > < / video >

    # test = match.group(1)
    # print('test:',test)
    print(video)
    src = video.attrs.get('src')

    print(src)


def getAllUrls(url):
    r0 = requests.get(url)
    match = re.search(r'pageSize = (\d+).+\n.+listTotal = (\d+)', r0.text, flags=re.M)
    pageSize = match.group(1)  # 40
    listTotal = match.group(2)
    pageend = int(listTotal) // int(pageSize) + 1  # 博客列表的最终页

    urllist = []
    for i in range(1, pageend + 1):
        pageurl = url + '/article/list/' + str(i)

        res = requests.get(pageurl)
        soup = BeautifulSoup(res.text, 'html.parser')
        divs = soup.find_all(name='div', attrs={'class': 'article-item-box csdn-tracking-statistics'})
        aas = [div.find('a') for div in divs]  # 获得包含文章链接的a标签
        urllist += [a.attrs.get('href') for a in aas]

    return urllist


def getPageView(url):
    '''
    url传入的是博客首页，用来或的访问量
    :param url:
    :return: 访问量
    '''
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    divs = soup.find('div', attrs={'class': 'data-info d-flex item-tiling'})
    dls = divs.find_all('dl')
    return int(dls[-1].attrs.get('title'))
