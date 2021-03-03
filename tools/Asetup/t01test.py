# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 5:20 下午
# @Author  : 百变金刚
# @Content :
from tools.Asetup.Operator import Operator


def add(a, b):
    op1 = Operator(a)
    op2 = Operator(b)
    print(op1.add(op2))

def sbutract(a, b):
    op1 = Operator(a)
    op2 = Operator(b)
    print(op1.subtract(op2))