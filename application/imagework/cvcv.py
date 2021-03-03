# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 7:22 下午
# @Author  : 百变金刚
# @Content :
import cv2

def test():
    ip = 'data/peotry.png'
    # ip = 'data/dog.jpg'
    img = cv2.imread(ip)

    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(img.shape)

if __name__ == '__main__':
    test()