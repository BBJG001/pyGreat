# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 3:47 下午
# @Author  : 百变金刚
# @Content :
import os


def fun1():
    cmd = 'echo $PATH'
    # res = os.system(cmd)
    res2 = os.popen(cmd)
    content = res2.read()
    cl = content.split(':')
    cl_ = ['export PATH="{}:$PATH"'.format(ci) for ci in cl]
    out = '\n'.join(cl_)
    print(out)

def fun2():
    strpath = ':/usr/local/go/bin:/usr/local/mysql/bin:/usr/local/mysql/support-files:/usr/local/sbin:/usr/local/bin::/usr/local/go/bin:/usr/local/mysql/bin:/usr/local/mysql/support-files:/usr/local/sbin:/usr/local/bin::/usr/local/go/bin:/usr/local/mysql/bin:/usr/local/mysql/support-files:/usr/local/sbin:/usr/local/bin:/Users/baibianjingang/.linuxbrew/bin:/Users/baibianjingang/.linuxbrew/sbin::/usr/local/go/bin:/usr/local/mysql/bin:/usr/local/mysql/support-files:/usr/local/sbin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/VMware Fusion.app/Contents/Public:/usr/local/go/bin'
    pl = strpath.split(':')
    pl_ = ['export PATH="{}:$PATH"'.format(pi) for pi in pl]
    out = '\n'.join(pl_)
    print(out)



if __name__ == '__main__':
    # fun1()
    fun2()
