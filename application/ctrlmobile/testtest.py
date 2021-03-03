# print(5//2)
import requests
from bs4 import BeautifulSoup

res = requests.get(r'https://sspai.com/post/23631')
soup = BeautifulSoup(res.text, 'lxml')
print(soup.__str__())