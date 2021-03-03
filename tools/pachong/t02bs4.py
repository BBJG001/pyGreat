# 爬取汽车之家网站
import requests
from bs4 import BeautifulSoup  # 解析html网页的

response = requests.get("https://www.autohome.com.cn/news/")  # 通过代码伪造浏览器发送get请求
response.encoding = 'gbk'  # 这个网站的编码是gbk，默认是utf-8，所以这里改一下

# print(response.text)      # 文本
# print(response.content)   # 二进制流，图片等写入文件传content

soup = BeautifulSoup(response.text, 'html.parser')

div = soup.find(name='div', attrs={'id': 'auto-channel-lazyload-article'})  # 通过标签筛选，找到与之匹配的第一个标签
# div = soup.find(name='div', id='auto-channel-lazyload-article')  # 应该也是可以这么写的
# name  标签名
# attrs 传属性字典
print(div)
li_list = div.find_all(name='li')  # 找到所有的匹配的标签
# 返回所以匹配对象的列表

with open('text', 'w', encoding='gbk') as f:
    f.write('')
    # 把内容写入文件

for li in li_list:

    title = li.find(name='h3')  # 找标题
    if not title:  # 删选掉空的
        continue
    p = li.find(name='p')  # 找简介
    a = li.find(name='a')  # 找链接

    with open('text', 'a') as f:
        f.write(title.text + '\n')  # 获取标签中间的内容
        f.write(a.attrs.get('href') + '\n')     # 获取标签的属性
        f.write(p.text + '\n')

    # print(title.text) #<h3>标题</h3>
    # print(a.attrs.get('href')) #a.attrs 以字典形式返回a标签的所有属性
    # print(p.text)

    # img = li.find(name='img')
    # src = img.get('src') #直接get，也可以获得属性
    # src = "https:" + src
    # print(src)

    # # 再次发起请求，下载图片
    # file_name = 'img/' + src.rsplit('/', maxsplit=1)[1]
    # ret = requests.get(src)
    # with open(file_name, 'wb') as f:  # 因为下载的是图片，wb
    #     f.write(ret.content)
    #     # ret.text 将结果ret转换成字符串，ret.content直接是二进制文件
print('over')
