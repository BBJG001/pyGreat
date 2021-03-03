# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 5:51 下午
# @Author  : 百变金刚
# @Content :
import os
import shutil

#
# https://www.cnblogs.com/Eva-J/articles/7228075.html#_label7

# 复杂的用shutil: https://docs.python.org/zh-cn/3/library/shutil.html

'''
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息

os.system("bash command")  运行shell命令，直接显示
os.popen("bash command).read()  运行shell命令，获取执行结果
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd

os.path
os.path.abspath(path) 返回path规范化的绝对路径os.path.split(path) 将path分割成目录和文件名二元组返回 
os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 
os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path) 返回path的大小
'''

'''
shutil.copyfile( src, dst)    # 从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
shutil.move( src, dst)        # 移动文件或重命名
shutil.copymode( src, dst)    # 只是会复制其权限其他的东西是不会被复制的
shutil.copystat( src, dst)    # 复制权限、最后访问时间、最后修改时间
shutil.copy( src, dst)        # 复制一个文件到一个文件或一个目录
shutil.copy2( src, dst)       # 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst)       # 如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree( olddir, newdir, True/Flase)
# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.rmtree( src )    # 递归删除一个目录以及目录内的所有内容

'''

ddir = ''

# 新建文件夹
os.mkdir(ddir)
os.makedirs(ddir, exist_ok=True)    # 安全创建
shutil.rmtree(ddir, ignore_errors=True)   # 递归删除，报错忽略

# 文件重命名
src = 'txx.txt'
dst = 'tyy.txt'
shutil.move( src, dst)        # 移动文件或重命名

# 删除
os.removedirs('dirname1')    # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.rmdir('dirname')    # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
shutil.rmtree('adir')    # 递归删除一个目录以及目录内的所有内容
os.remove('afile')  # 删除一个文件
