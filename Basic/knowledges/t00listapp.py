# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 6:42 下午
# @Author  : 百变金刚
# @Content : application to list

# 2D sort by one col
def sortbycol(arr, colid):
    arr.sort(key=lambda x:x[colid], reverse=False)
    # sorted(arr, key=lambda x:x[colid])
    return arr

def testsortbc():
    arr = [[1,2,3], [3,1,4], [5,3,9]]
    arred = sortbycol(arr, 1)
    for ai in arred:
        print(ai)

if __name__ == '__main__':
    testsortbc()
