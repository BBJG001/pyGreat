import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 设置字体，支持中文显示
matplotlib.rcParams['font.family'] = 'STSong'

# 生成测试数据
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 图表的标题
plt.title("图标题")

# 设置x轴，y轴的取值范围
plt.xlim(-1, 2)
plt.ylim(-2, 3)

# 设置x轴，y轴的刻度显示
plt.xticks(np.linspace(-1, 2, 5))
plt.yticks([-2, 1, 1.5, 2, 2.5, 3], [r'(-2)', r'及格(1)', r'中(1.5)', r'良(2)', r'优(2.5)', r'(3)'])

# 设置x轴，y轴属性
plt.xlabel('时间')
plt.ylabel('销量')

# 设置图像边框
ax = plt.gca()
# ax.spines['top']选一个轴，上下左右四个轴
# top   bottom  left    right

# 设置右轴，这是none，即选默认色——白色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x坐标（xaxis）刻度的位置，可选（所有位置：top，bottom，both，default，none）
ax.xaxis.set_ticks_position('top')

# 设置底轴
# 位置所有属性：outward，axes，data
# outward：偏离x轴的值，单位貌似是像素
# axes：取值[0,1]，占y轴的百分比
# data：意为按y轴的值取位置
ax.spines['bottom'].set_position(('data', -1))  # ylim（-2，3），

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0.5))

plt.show()
