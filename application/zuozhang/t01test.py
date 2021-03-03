# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 2:20 下午
# @Author  : 百变金刚
# @Content : test for zuozhang

ddin = {'奖学金':4000, '工资': 7000*2, '补助': 600, '退租房押金': 2300,
        # '补助': 300, '优干': 600, '导师补助': 800,
        }
ddout = {'房租': 3000*4,
         '中介费': 1500,
         }

def operator():
    print(sum(ddin.values())-sum(ddout.values()))

if __name__ == '__main__':
    operator()
