# 这个还会要求先访问首页，才能点赞
import requests
# 1. 查看首页
r1 = requests.get( #返回r1一个非授权的cookie
    url='https://dig.chouti.com/',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
)

# 2. 提交用户名和密码
r2 = requests.post(
    url='https://dig.chouti.com/login',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    },
    data={
        'phone':'8613121758648',
        'password':'woshiniba',
        'oneMonth':1
    },
    cookies=r1.cookies.get_dict()#带着从r1那里带的cookie去
)


# 3. 点赞
r3 = requests.post(
    url='https://dig.chouti.com/link/vote?linksId=20435396',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    },
    cookies=r1.cookies.get_dict()
)
print(r3.text)