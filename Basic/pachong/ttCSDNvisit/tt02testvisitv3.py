# 将某用户的CSDN所有博客访问一遍
# 通过代理proxy
import requests
from bs4 import BeautifulSoup  # 解析html网页的
import re
import json

def getaPageData(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    divs = soup.find_all(name='div', attrs={'class': 'article-item-box csdn-tracking-statistics'})
    aas = [div.find('a') for div in divs]  # 获得包含文章链接的a标签
    return [a.attrs.get('href') for a in aas]

def vistapagearticle(link, proxies):
    res = requests.get(
        url=link,
        proxies=proxies
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    div = soup.find(name='div', attrs={'class': 'article-list'})
    # find：找到阈值相匹配的第一个标签
    # 案例说通过class进行find是不太好的，因为不同的标签的class值可能是相同，这里我通过查看源码确认了该class值只在这个div才有
    # 通过id寻找是一种比较准确的方式，因为通过id匹配是唯一的

    h4_list = div.find_all(name='h4')
    # find_all：找对与之相匹配的所有标签
    a_list = [h4.find(name='a') for h4 in h4_list]

    for a in a_list:
        link = a.attrs.get('href')

        res2 = requests.get(link)

        # 打印一下进度
        print('\r[', str(a_list.index(a) + 1).rjust(2, ' '), '/', len(a_list), ' ]', end='')
    print()


if __name__ == '__main__':
    # indexurl = 'https://blog.csdn.net/BBJG_001'
    indexurl = 'https://blog.csdn.net/willow_zhu'

    r0 = requests.get(indexurl)
    match = re.search(r'pageSize = (\d+).+\n.+listTotal = (\d+)', r0.text, flags=re.M)
    pageSize = match.group(1)   # 40
    listTotal = match.group(2)
    pageend = int(listTotal) // int(pageSize) + 1   # 博客列表的最终页

    iplist = []
    with open('../data/ip.txt', 'r') as f:
        ips = json.load(f)
        for cell in ips:
            iplist.append(cell['address']+':'+cell['port'])



    for epoch in range(10):
        print('epoch:', epoch, '-------------------------')
        for i in range(1, pageend+1):
            for ip in iplist:
                proxies = {'http': 'http' + ip, 'https': 'https' + ip}
                print( str(i), '/', pageend, 'processing . . .')
                url = indexurl + '/article/list/' + str(i)
                # vistapagearticle(url, proxies)
                try:
                    vistapagearticle(url, proxies)
                except:
                    break

