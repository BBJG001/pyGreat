import numpy as np

# numpy是c语言实现的，只是对python封装了接口

# copy 与 view（切片）
# copy（就是所说的深copy），是真正的在内存中另外开辟空间，复制一份
# view，没有对应方法，就是切片，这个切片实际上并没有另外开辟内存空间，只是将原来变量的中间索引传给了新变量，所以就快了（不用开辟新空间）

a = np.arange(1, 7).reshape((3,2))
a_view = a[:2]
a_copy = a[:2].copy()

# 将矩阵展平（拉成一维）
# 对于 view 还有一点要提, 你是不是偶尔有时候要把一个矩阵展平,
# 用到 np.flatten() 或者 np.ravel(). 他俩是不同的! ravel 返回的是一个 view
# .ravel()会在需要copy的时候在执行copy
print(a)
print(a.flatten())
print(a)
print(a.ravel())