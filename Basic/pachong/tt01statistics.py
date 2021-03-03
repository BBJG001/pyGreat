import requests
from bs4 import BeautifulSoup  # 解析html网页的
import re
import matplotlib.pyplot as plt


def getaPageData(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    divs = soup.find_all(name='div', attrs={'class': 'article-item-box csdn-tracking-statistics'})
    aas = [div.find('a') for div in divs]  # 获得包含文章链接的a标签
    spans = [div.find(name='span', attrs={'class': 'num'}) for div in divs]  # 获得包含阅读量的span
    return {a.attrs.get('href'): int(span.text) for a, span in zip(aas, spans)}  # 封装成字典返回


if __name__ == '__main__':
    indexurl = 'https://blog.csdn.net/BBJG_001'
    baseurl = 'https://blog.csdn.net/BBJG_001/article/list/'
    r0 = requests.get(indexurl)
    alldata = {}

    match = re.search(r'pageSize = (\d+).+\n.+listTotal = (\d+)', r0.text, flags=re.M)
    pageSize = match.group(1)  # 40
    listTotal = match.group(2)  # 152
    pages = int(listTotal) // int(pageSize) + 1
    for i in range(1, pages + 1):
        url = baseurl + str(i)
        datai = getaPageData(url)
        alldata.update(datai)  # 向alldata中追加本轮url的数据

    print('最受欢迎的文章：', max(alldata, key=alldata.get))  # 返回字典中最大值对应的key

    plt.bar(range(len(alldata)), list(alldata.values()))  # 柱状图

    plt.ylim(0, 250)  # 为了不使结果看着太过悬殊，限制y轴高度

    plt.show()
