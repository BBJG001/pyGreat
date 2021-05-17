import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# # 设置字体，支持中文显示
# matplotlib.rcParams['font.family'] = 'STSong'
plt.rcParams['font.sans-serif'] = ['Times New Roman']
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

# plt.figure()

# 设置x轴，y轴的值范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置x轴的显示
plt.xticks(np.linspace(-1, 2, 5))
# 设置y轴的显示
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'really bad', r'bad', r'normal', r'good', 'really\ngood'])

# 写法一：画图并设置图例，label值为图例内容
plt.plot(x, y1, label='linear line')
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
plt.legend(loc=4)
'''
**loc=4**
或
**loc='lower right'**
    'best': 0,
    'upper right': 1,
    'upper left': 2,
    'lower left': 3,
    'lower right': 4,
    'right': 5,
    'center left': 6,
    'center right': 7,
    'lower center': 8,
    'upper center': 9,
    'center': 10,
'''

# 写法二：先画图，后面一并设置图例，注意变量的写法，需要加一个逗号‘,’
# l1, = plt.plot(x, y1)
# l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
# plt.legend(handles=[l1, l2], labels=['label1', 'label2'], loc='best')

plt.show()
