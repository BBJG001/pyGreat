# 将某用户的CSDN所有博客访问一遍
# 在testvisit基础上的改进，统一获得urls列表，再进行访问
# v1_async版本
# 好像不太行，时间间隔的问题
import requests
from bs4 import BeautifulSoup  # 解析html网页的
import re
import asyncio
import aiohttp
import time

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

async def visit(session, url):
    print(url)
    # response = None
    try:
        response = await session.get(url)       # 等待并切换
    except:
        pass
    # return response

async def main(loop, urls):
    async with aiohttp.ClientSession() as session:  # 官网推荐建立 Session 的形式
        tasks = [loop.create_task(visit(session, url)) for url in urls]
        finished, unfinished = await asyncio.wait(tasks)

if __name__ == '__main__':
    # indexurl = 'https://blog.csdn.net/BBJG_001'
    # indexurl = 'https://blog.csdn.net/willow_zhu'
    indexurl = 'https://blog.csdn.net/komorebi6'

    urls = getAllUrls(indexurl)
    u_total = len(urls)
    readnums = getPageView(indexurl)
    print('当前访问：', readnums)

    loop = asyncio.get_event_loop()
    for i in range(10):
        ts = time.time()

        loop.run_until_complete(main(loop, urls))

        te = time.time()
        print('单轮耗时：', te-ts)

        readnume = getPageView(indexurl)
        print('当前访问：', readnume)
        print('访问增加：', readnume-readnums)
    loop.close()