import numpy as np

# a = [1]
# b = [2]
# np.dot(a, b)        # 矩阵乘法，*并不是
# np.exp()        # 自然对数？e？
# np.pi           # pai
#
# np.linalg.pinv()        # 求伪逆矩阵
# np.linalg.inv()        # 求逆矩阵

# # 生成全0的数组
# print('np.zeros(5)\n', np.zeros(5))
# print('np.zeros(5, dtype=int)\n', np.zeros(5, dtype=int))
# print('np.zeros((3, 7))\n', np.zeros((3, 7)))

# 生成全1的数组
# print('np.ones(5)\n', np.ones(5))
# print('np.ones(5, dtype=int)\n', np.ones(5, dtype=int))
# print('np.ones((3, 7)\n', np.ones((3, 7)))

# # 生成一组无意义的数
# print('np.empty(5)\n', np.empty(5))
# print('np.empty(5, dtype=int)\n', np.empty(5, dtype=int))


# np生成序列
# # 生成指定公差的等差数列np.arange()
# # 是含首不含尾的
# print('np.arange(0, 10, 2)\n', np.arange(0, 10, 2))
# print('np.arange(0., 10., 2.)\n', np.arange(0., 10., 2.))
# print('np.arange(0, 10, 2, dtype=np.float32)\n', np.arange(0, 10, 2, dtype=np.float32))

# # 生成指定数量的等差数列np.linspace()
# # 首尾皆包含的
# print('np.linspace(1, 2, 10)\n', np.linspace(1, 2, 10))
# # 指定不包含尾项
# print('np.linspace(1, 2, 10)\n', np.linspace(1, 2, 10, endpoint=False))

# # 生成指定数量的等比数列np.logspace()
# print('np.logspace(0, 5, 5)\n', np.logspace(0, 5, 6))
# # np.logspace(0, 5, 6)意为生成10**0到10**5，包含6个数的等比数列
# print('np.logspace(0, 5, 5, endpoint=False)\n', np.logspace(0, 5, 6, endpoint=False))
# # 当然也可以自定义基数，通过设置base属性
# print('np.logspace(0, 5, 5, base=2)\n', np.logspace(0, 5, 6, base=2))

# numpy生成随机序列
# numpy的随机序列生成的功能写在numpy.random下
# np.random.seed(1) 计算机中所谓的随机实际上有有迹可循的，通过这个seed的设置可以让每次生成相同的随机数，传的参数为一个int值
np.random.seed(1)

# # np.random.rand()生成0-1之间的随机小数，如果不传参数，返回一个随机数，传的参数为数组中元素的个数
# print('np.random.rand()\n', np.random.rand())
# print('np.random.rand(10)\n', np.random.rand(10))

# # np.random.randn(n) 返回包含n个元素的符合正太分布的数组
# print('np.random.randn(10)\n', np.random.randn(10))

# # np.random.randint(1, 10, 5)生成[1, 10)之间的5个随机整数
# print('np.random.randint(1, 10, 5)\n', np.random.randint(1, 10, 5))

# # np.random.random_integers(1, 10, 5)生成[1, 10]之间的5个随机整数
# print('np.random.random_integers(1, 10, 5)\n', np.random.random_integers(1, 10, 5))

# # np.random.shuffle(ll)，将ll数组打乱顺序
ll = np.arange(10)
print('ll=\n', ll)
np.random.shuffle(ll)
print('after np.random.shuffle(ll)\n', ll)












# 有几个常用的函数如下：
#
# random.random()
# 产生一个0-1之间的随机数
#
# random.uniform(1,10)
# 产生一个1-10之间均匀分布的随机数
#
# random.randint(1,10)
# 在1-10之间产生一个随机的整数
#
# random.ranrange(0,100,2)
# 从range(0,100,2)中随机选取序列中的一个数
#
# random.choice([‘lan’,’wang’,’zhang’])
# 从序列中随机选取一个某个元素
#
# random.shuffle([1,2,3,4,5])
# 随机打乱一个序列
#
# random.sample([1,2,3,4,5],3)






# # 自己造一个等比数列
# ll = [2**v for v in range(3, 8)]
# print(ll)





