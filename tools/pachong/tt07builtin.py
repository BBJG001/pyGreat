import requests
from bs4 import BeautifulSoup

url = 'https://www.runoob.com/python3/python3-built-in-functions.html'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

tbody = soup.find('tbody')

tds = tbody.find_all('td')

tdtextl = [td.text for td in tds]
tl = sorted(tdtextl)
tl = tl[:-2]

text = ['- <strong id="{}">{}</strong>\n\n  ```python\n  \n  ```\n'.format(cell[:-2], cell) for cell in tl]
for i in text:
    print(i, end='')


ss = '| | |内置函数 | | |\n|---|---|---|---|---|\n'
for i in range(len(tl)):
    if i % 5 == 0:
        ss += '|'
    ss += '[{}](#{})|'.format(tl[i], tl[i][:-2])
    if (i + 1) % 5 == 0:
        ss += '\n'
if len(text) % 5 != 0:
    ss += '\n'

# print(ss)
