# 在pycarm中相对导入会报红，但是可以运行
# import
# form
# as
# *
# __name__
# 都支持多名字导入
# sys.moudles记录了所有被导入的模块
# sys.path 记录了导入模块的时候寻找的所有路径

# from import
# from 模块名 import 变量名
    #直接使用 变量名 就可以完成操作
    #如果本文件中有相同的变量名会发生冲突
# from 模块名 import 变量名字 as 重命名变量名
# from 模块名 import 变量名1，变量名2
# from 模块名 import *
    # 将模块中的所有变量名都放到内存中
    # 如果本文件中有相同的变量名会发生冲突
# from 模块名 import * 和 __all__ 是一对
    # 没有这个变量，就会导入所有的名字
    # 如果有all 只导入all列表中的名字
# __name__
# 在模块中 有一个变量__name__，
# 当我们直接执行这个模块的时候，__name__ == '__main__'
# 当我们执行其他模块，在其他模块中引用这个模块的时候，这个模块中的__name__ == '模块的名字'

#------ 模块导入的过程
# 先从sys.modules里查看是否已经被导入
# 如果没有被导入，就依据sys.path路径取寻找模块
# 找到了就导入
# 创建这个模块的命名空间
# 执行文件，把文件中的名字都放到命名空间里
# import sys
# print(sys.modules.keys())
# print(sys.path)

# import sys
# sys.path.insert(0,'C:\\Users\\Administrator\\PycharmProjects\\s9\\day21\\dir')
# # print(sys.path)
# from glance.api import policy

# 使用绝对路径 不管在包内部还是外部 导入了就能用
# 不能挪动，但是直观

# from dir import glance
# glance.api.policy.get()
# 相对路径
# 可以随意移动包 只要能找到包的位置，就可以使用包里的模块
# 包里的模块如果想使用其它模块的内容只能使用相对路径，使用了相对路径就不能在包内直接执行了