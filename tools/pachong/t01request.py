# https://www.cnblogs.com/wupeiqi/articles/6283017.html
import requests


res = requests.get(
    url='https://blog.csdn.net/BBJG_001',   # 我的CSDN个人主页
)

print(res.url)
# https://blog.csdn.net/BBJG_001
print(res.text)     # 查看整个网页（html的形式），就是在浏览器中查看网页源代码所看到的的内容
# 这里只截取开始几行来显示
# <!DOCTYPE html>
# <html lang="zh-CN">
# <head>
#     <meta charset="UTF-8">
#     <link rel="canonical" href="https://blog.csdn.net/BBJG_001"/>