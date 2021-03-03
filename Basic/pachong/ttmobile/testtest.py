import requests
from bs4 import BeautifulSoup

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'http://www.wodedy.net/play/145-0-0.html'
}

urls = ['http://www.wodedy.net/play/145-0-%d.html'%i for i in range(4)]
for u in urls:
    pass

url = 'http://www.wodedy.net/play/145-0-0.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
div = soup.find('div', attrs={'id':'vlink_1'})
print(div)
print('第1集' in res.text)
src = 'https://s1.xiahi.com/dm/jianyuzhanjian.Vol.01.mp4'
r = requests.get(src, headers=HEADER, stream=True)

with open(r'E:\Test\JYZJ\over\v1.mp4', 'wb') as f:   # 注意文件处理模式为‘wb’（以二进制写入）
    f.write(r.content)
