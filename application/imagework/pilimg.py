# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 7:22 下午
# @Author  : 百变金刚
# @Content :
from PIL import Image

def test():
    ip = 'data/poetry.png'
    img = Image.open(ip)
    print(img.__dict__)

if __name__ == '__main__':
    test()