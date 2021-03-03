import requests

url = 'test'

r = requests.post(
    url,
    headers={},
    data={
        'username': 'name',
        'password': 'pwd',
    }
)

res = requests.get(
    url,
    headers={},
    # cookies = r.cookies.get_dict(),
    cookies = r.cookies,    # 莫烦这么写的
)

#-------------------------- session
# 每次带上cookies未免有些麻烦，requests中的session可以自行保存下cookies，不用每次都传入
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
# {'username': 'Morvan', 'loggedin': '1'}

r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)