import re
import requests

r1 = requests.get(
    url='https://passport.lagou.com/login/login.html',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
)
X_Anti_Forge_Token = re.findall("X_Anti_Forge_Token = '(.*?)'", r1.text, re.S)[0]
X_Anti_Forge_Code = re.findall("X_Anti_Forge_Code = '(.*?)'", r1.text, re.S)[0]
# print(X_Anti_Forge_Token, X_Anti_Forge_Code)
# print(r1.text)
#
r2 = requests.post(
    url='https://passport.lagou.com/login/login.json',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Anit-Forge-Code':X_Anti_Forge_Code,
        'X-Anit-Forge-Token':X_Anti_Forge_Token,
        'Referer': 'https://passport.lagou.com/login/login.html', # 上一次请求地址是什么？
    },
    data={
        "isValidate": True,
        'username': '15131255089',
        'password': 'ab18d270d7126ea65915c50288c22c0d',
        'request_form_verifyCode': '',
        'submit': ''
    },
    cookies=r1.cookies.get_dict()
)
print(r2.text)