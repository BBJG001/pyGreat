# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 11:13 上午
# @Author  : 百变金刚
# @Content : 实现可参考 https://gine.me/posts/d00e0623063b4edf843d571850c39f95
import yaml

class Conf():
    def __init__(self, p_conf):
        with open(p_conf) as f:
            conf = yaml.safe_load(f)
        eval('self.')
        # 暂时放弃，yaml的类型有些多，尚无法想到比较合理的方案，挂入计划