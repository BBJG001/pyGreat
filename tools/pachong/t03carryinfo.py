import requests
from bs4 import BeautifulSoup

# 有些网站会做限制，需要获得浏览器的一些信息，无这些信息将不会响应访问
# 通过header设置这些信息
# F12   、   Ctrl+Shift+I    、   网页上右击 =》检查
r1 = requests.get(
    url='https://dig.chouti.com/',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
        # 这里还可以以字典形式给出别的请求头属性
    }
)

soup = BeautifulSoup(r1.text,'html.parser')

# 标签对象
content_body = soup.find(name='div', attrs={'class':'link-con'})
# print(content_list)
# [标签对象,标签对象]
title_list = content_body.find_all(name='div',attrs={'class':'link-detail'})
for title in title_list:
    a = title.find(name='a',attrs={'class':'link-title link-statistics'})
    # print(a.attrs.get('href'))
    print(a.text)   # 获得a便签中的标题文字
# 这里只给出几个以供示例
# 三个男朋友，该如何取舍？
# 设计师自制概念视频：如果用苹果风格来设计 Windows 10（YouTube Avdan）
# 日本bauhutte公司设计的gaming bed“肥宅快乐床”，可以躺一辈子了