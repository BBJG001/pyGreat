# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 5:59 下午
# @Author  : 百变金刚
# @Content :

class Operate():
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def add(self):
        return self.x+self.y

    def minus(self):
        return self.x-self.y

    def multi(self):
        return self.x*self.y

    def divide(self):
        return self.x/self.y
