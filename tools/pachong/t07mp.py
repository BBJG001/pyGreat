import multiprocessing as mp
import requests
from bs4 import BeautifulSoup  # 解析html网页的
import re
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


def job(url):
    return requests.get(url)

if __name__ == '__main__':
    indexurl = 'https://blog.csdn.net/BBJG_001'

    urls = getAllUrls(indexurl)

    ts = time.time()
    res = []
    for u in urls[:20]:
        res.append(requests.get(u))
        # 为了单纯看效果，这里就不在增加其他操作
    print('串行耗时：', time.time()-ts)
    # 串行耗时： 7.231183767318726
    # print(res[0].text)    # 打印结果观察

    ts = time.time()
    pool = mp.Pool(5)
    multi_res = [pool.apply_async(job, (url,)) for url in urls[:20]]
    print('多进程耗时:', time.time() - ts)
    # 多进程耗时: 0.0679936408996582
    # print(multi_res[0].get().text)    # 打印结果观察
