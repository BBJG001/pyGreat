import requests
import re
import json
from bs4 import BeautifulSoup

# url = 'https://zhuanlan.zhihu.com/api/columns/reinforcementlearning/articles?include=data&limit=100&offset=0'
# url = 'https://zhuanlan.zhihu.com/api/columns/reinforcementlearning/articles?include=data&limit=100&offset=100'
# res = requests.get(
#     url=url,
#     headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
#         # 这里还可以以字典形式给出别的请求头属性
#     }
# )
# res.encoding = 'unicode_escape'
# print(res.text)
#
# with open('data/resall.html', 'w', encoding='unicode_escape') as f:
#     f.write(res.text)

# strtest = '"voting": 0, "title": "【强化学习 110】Reward-Free Exploration", "url": "https://zhuanlan.zhihu.com/p/111672225", "comment_permiss'*2
# sb = strtest.encode('utf8')
# print(sb)
# # res = re.findall(r'"title":\s".+", "url":".+",', strtest)
# res = re.findall(r'"title":\s"(.+?)",\s"url":\s"(.+?)",', strtest)
# print(res)

# lx = list(range(5))
# ly = list(range(10, 15))
# print(zip(lx, ly))
# for x, y in zip(lx, ly):
#     print(x,y)
# lxy0 = [(0,10),(1,11), (2,12)]
# for x,y in lxy0:
#     print(x,'--',y)
#
# lxy = [(x, y) for x in range(5) for y in range(10, 15)]
# print(lxy)

HEADERS={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
        # 这里还可以以字典形式给出别的请求头属性
}
#
# zhuanlan = 'reinforcementlearning'
# urlpage = 'https://zhuanlan.zhihu.com/api/columns/{}/articles?include=data&limit={}&offset={}'.format(zhuanlan, 100, 0)
# respage = requests.get(urlpage, headers=HEADERS)
# content = json.loads(respage.text)
# print(content)
# p_numbers.extend([item['id'] for item in content['data']])
# p_titles.extend([item['title'] for item in content['data']])

url = 'https://zhuanlan.zhihu.com/p/118422846'
res = requests.get(url, headers=HEADERS).text

title = re.search(r'<h1\sclass="Post-Title">(.+)</h1>', res).group(1)
print(title)
