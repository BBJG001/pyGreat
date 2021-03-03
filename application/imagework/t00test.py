# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 7:23 下午
# @Author  : 百变金刚
# @Content :
# python 图片 数组到二进制的互相转换 https://blog.csdn.net/chenpe32cp/article/details/92817084
import cv2
import numpy as np
import re
from io import BytesIO

from wand.display import display
from wand.image import Image as Img
from wand.drawing import Drawing
from wand.color import Color
from PIL import Image
import numpy as np

class ImgHelper():
    '''
    转换
    保存
    show
    '''
    def __init__(self):
        # self.content
        # self.opil
        # self.ocv
        # self.oplt
        pass

    def getWidth(self):
        return 5
    @property   # 实现通过函数返回类的一个属性
    def width(self):
        """(:class:`numbers.Integral`) The width of this image."""
        return self.getWidth()

    def topil(self, arr):
        pass

    def tocv(self, arr):
        pass

    def toplt(self, arr):
        pass

    def bin2img(self, content):
        pass

    def pil2arr(self, ojb):
        pass

def testcvbybin():
    src=cv2.imread("data/dog.jpg",1)
    src.tofile("data/emma.bin") #将jpg图片保存到二进制文件

    src2=np.fromfile("data/emma.bin",dtype=np.uint8) #从二进制文件恢复图片，注意dtype格式要与src一致
    src2=np.reshape(src2,src.shape) #从二进制读取的数据是一维的，需要恢复到原图一致的维度

    print(src)

    # cv2.namedWindow("Image")
    cv2.imshow("src2",src2)
    cv2.waitKey(0)
    cv2.imshow("src",src)
    cv2.waitKey(0)

def testwand():
    with Img(filename='data/poetry.png') as img:
        # 生成指向图片QingYi.jpg的图片对象img，用with打开图片用完不必关闭
        print(img.__dict__)
        print()

        print('width =', img.width)
        # 通过图片对象的属性width获得图片的宽，输出：width = 334
        # print('height =', img.height)	# 图片的高，height = 504
        # print('format: ', img.format)
        # 图片的格式，输出为：format = JPEG，format是图片对象的一个属性，不一定与图片的保存格式相同
        # print('size: ', img.size)		# 图片的尺寸，size：(334, 504)

        # img.save(filename='ballet.png')	# 保存时转换图片保存格式为png
        # print('format: ', img.format)
        # format的属性值还是jpeg，跟输出格式没关系的属性

        # display(img)    # 打开img对象所指的图片文件，实参必须是Image对象

if __name__ == '__main__':
    # testcvbybin()
    testwand()