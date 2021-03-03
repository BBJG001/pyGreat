# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 5:16 下午
# @Author  : 百变金刚
# @Content :

class Operator():
    def __init__(self, val):
        self.val = val

    # 只为测试
    def add(self, op):
        return self.val+op.val

    def subtract(self, op):
        self.val -= op.val
