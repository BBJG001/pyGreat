# 将某用户的CSDN所有博客访问一遍
# 多线程
# 结果：统一获得所有url再进行访问会加快；单纯的多进程因为访问太频繁（两次间隔太短）而无法获得预期访问量增加量
import requests
from bs4 import BeautifulSoup  # 解析html网页的
import re
import multiprocessing as mp
from multiprocessing import Manager
import time


def job(urllist, resdict, restp, lock):
    for u in urllist:
        res = requests.get(u)
    with lock:
        resdict['num_p'] += 1
        restp.value -= 1
        resdict['num_url'] += len(urllist)


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
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    divs = soup.find('div', attrs={'class': 'data-info d-flex item-tiling'})
    dls = divs.find_all('dl')
    return int(dls[-1].attrs.get('title'))


if __name__ == '__main__':
    indexurl = 'https://blog.csdn.net/BBJG_001'
    # indexurl = 'https://blog.csdn.net/willow_zhu'

    manager = Manager()
    res_dict = manager.dict({'num_p': 0, 'num_url': 0})
    p_num = manager.Value('n', 2)
    lock = manager.Lock()

    urls = getAllUrls(indexurl)
    print('当前访问量：', getPageView(indexurl))

    # 没有找到pool不阻塞父进程的方案
    '''
    pool = mp.Pool(processes=2)
    print(res_dict)
    # print([(urls, res_dict)] * 2)

    # pool.map(job, [(urls, res_dict)]*2)
    # pool.map(job, zip([urls]*2, [res_dict]*2))
    pool.starmap(job, [(urls, res_dict, lock)]*2)
    '''

    nn = p_num.value
    for e in range(nn):
        p = mp.Process(target=job, args=(urls, res_dict, p_num, lock))
        # 生成进程，并传入要执行的操作（函数），args=参数列表，只传一个参数的时候注意要在参数后面加一个逗号，因为args需要一个可迭代的参量
        p.start()  # 进程操作开始执行

    while (True):
        # time.sleep(5)
        # print(res_dict['num_p'])
        time.sleep(1)
        if p_num.value == 0:
            print('访问了', res_dict['num_url'], '次')
            print('当前访问量：', getPageView(indexurl))
            break
