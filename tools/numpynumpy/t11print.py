import numpy as np

np.random.seed(1)   # 控制每次生成的随机数据相同

data = np.random.random(700).reshape((100,7))
print(data)

np.set_printoptions(
    infstr='inf',
    nanstr='nan',
    formatter=None,
    precision=2,    # 精度，保留小数点后几位
    threshold=500,
    # 最多可现实的Array元素个数
    # 限制的是基本元素个数，如3*5的矩阵，限制的是15而非3（行）
    # 如果超过就采用缩略显示
    edgeitems=3,
    # 在缩率显示时在起始和默认显示的元素个数
    linewidth=150,  # 每行最多显示的字符数，默认80，超过则换行显示
    suppress=True   # 浮点显示（不用科学计数法）
)
print(data)