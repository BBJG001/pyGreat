import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 随机生成1000个数据
data = pd.Series(np.random.randn(1000), index=np.arange(1000))

# 为了方便观看效果, 我们累加这个数据
data = data.cumsum()

# pandas 数据可以直接观看其可视化形式
data.plot()

plt.show()

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
# columns的数据会自动生成在画图的图例中
# 每列出一条曲线，这个有四列，就是四条曲线
data = data.cumsum()
data.plot()
plt.show()

# 画图并返回一个画布
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
# 将下面这个 data 画在上一个 ax 上面
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
# 出图
plt.show()