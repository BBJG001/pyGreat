import requests
import re
import os
import json
import pdfkit

HEADERS={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
        # 这里还可以以字典形式给出别的请求头属性
}
# 如果配置了环境变量无法立即生效（大概是需要重启），可以通过这一行语句添加环境变量
os.environ["PATH"] += os.pathsep + r'C:\Program Files\wkhtmltopdf\bin'

def getUrls(zhuanlan):
    '''
    :param zhuanlan: such as https://zhuanlan.zhihu.com/reinforcementlearning   传入的是最后这个reinforcementlearning
    :return: 返回专栏下所有文章的url
    '''
    urls = []
    # p_titles = []
    offset = 0
    while True:
        url = 'https://zhuanlan.zhihu.com/api/columns/{}/articles?include=data&limit=100&offset={}'.format(zhuanlan, offset)
        html_string = requests.get(url,headers=HEADERS).text
        content = json.loads(html_string)   # 获取的content可以加载为json格式
        urls.extend([item['url'] for item in content['data']])  # 就可以用json的方式索引到所有的url
        # p_titles.extend([item['title'] for item in content['data']])  # 获取标题
        if len(content['data']) < 100:  # 如果是最后一页
            break
        else:
            offset += 100
    return urls

def getUrls2(zhuanlan):
    '''
    :param zhuanlan: such as https://zhuanlan.zhihu.com/reinforcementlearning   传入的是最后这个reinforcementlearning
    :return: 返回专栏下所有文章的url
    '''
    urlindex = 'https://zhuanlan.zhihu.com/{}'.format(zhuanlan)
    resindex = requests.get(urlindex, headers=HEADERS)
    # print(resindex.text)
    matchac = re.search(r'"articlesCount":(\d+),', resindex.text)   # 通过正则表达式获取文章总数
    articlesCount = int(matchac.group(1))
    upper = articlesCount//100+1  # 下面设置了每页显示100条，这里求总页数
    urls = []
    for i in range(upper):
        urlpage = 'https://zhuanlan.zhihu.com/api/columns/{}/articles?include=data&limit={}&offset={}'.format(zhuanlan, 100, 100*i)
        # limit最大是100
        respage = requests.get(urlpage, headers=HEADERS)
        respage.encoding = 'unicode_escape'
        matchurl = re.findall(r'"title":\s"[^"]+?",\s"url":\s"([^"]+?)",', respage.text)    # 通过正则匹配url
        urls+=matchurl
    return urls


def saveArticlesPdf(urls, target_path):
    os.makedirs(target_path, exist_ok=True)
    for i, url in enumerate(urls):
        print('[ {} / {} ] processing'.format(str(i+1).zfill(3), len(urls)))
        content = requests.get(url, headers=HEADERS).text
        title = re.search(r'<h1\sclass="Post-Title">(.+)</h1>', content).group(1)
        content = content.replace('<noscript>', '')     # 解决无法下载图片问题，其中图片路径为相对路径
        content = content.replace('</noscript>', '')
        try:
            # 方式一，直接调用wkhtmltopdf的命令
            # os.system('wkhtmltopdf {} {}'.format(content, target_path+'/{}.pdf'.format(title)))

            # 方式二，调用pdfkit包的方式
            pdfkit.from_string(content, target_path+'/{}.pdf'.format(title))
        except ValueError as e:
            print(title, e)


if __name__ == '__main__':
    zhuanlan = 'reinforcementlearning'
    # urls = getUrls(zhuanlan)
    urls = getUrls2(zhuanlan)
    saveArticlesPdf(urls, 'data/{}'.format(zhuanlan))
