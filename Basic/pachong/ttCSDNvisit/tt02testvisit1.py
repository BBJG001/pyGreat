# 将某用户的CSDN所有博客访问一遍
import requests
from bs4 import BeautifulSoup  # 解析html网页的
import re
import time

def vistapagearticles(link):
    res = requests.get(
        url=link,
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    div = soup.find(name='div', attrs={'class': 'article-list'})
    # find：找到阈值相匹配的第一个标签
    # 案例说通过class进行find是不太好的，因为不同的标签的class值可能是相同，这里我通过查看源码确认了该class值只在这个div才有
    # 通过id寻找是一种比较准确的方式，因为通过id匹配是唯一的

    h4_list = div.find_all(name='h4')
    # find_all：找对与之相匹配的所有标签
    a_list = [h4.find(name='a') for h4 in h4_list]

    urls = [a.attrs.get('href') for a in a_list]

    for url in urls:
        res2 = requests.get(url)
        # 打印一下进度
        print('\r[', str(urls.index(url) + 1).rjust(2, ' '), '/', len(a_list), ' ]', end='')
    print()


if __name__ == '__main__':
    # indexurl = 'https://blog.csdn.net/BBJG_001'
    # indexurl = 'https://blog.csdn.net/willow_zhu'
    indexurl = 'https://blog.csdn.net/komorebi6'

    r0 = requests.get(indexurl)
    match = re.search(r'pageSize = (\d+).+\n.+listTotal = (\d+)', r0.text, flags=re.M)
    pageSize = int(match.group(1))  # 40
    listTotal = int(match.group(2))  # 152
    pageend = listTotal // pageSize + 1  # 博客列表的最终页
    timegsp = 60 - 0.5 * listTotal if listTotal < 120 else 0

    for epoch in range(100):
        print('epoch:', epoch+1, '-------------------------')
        for i in range(1, pageend + 1):
            print('Page', str(i), '/', pageend, 'processing . . .')
            url = indexurl + '/article/list/' + str(i)
            vistapagearticles(url)
        time.sleep(timegsp)
