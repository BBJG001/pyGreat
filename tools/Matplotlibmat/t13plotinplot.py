# 导入pyplot模块
import matplotlib.pyplot as plt

# 初始化figure
fig = plt.figure()

# 创建数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# 作图左下角的坐标，在画布上的坐标，画布以左下角为圆点，向右向上为正方向，取值在[0,1]上，表示占长宽大小的比例
left, bottom = 0.1, 0.1
# 作图的宽高，取值在[0,1]上，表示占长宽大小的比例
width, height = 0.8, 0.8

ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r') # ‘r’ red
# 设置x轴，y轴属性说明文字
ax1.set_xlabel('x')
ax1.set_ylabel('y')
# 标题
ax1.set_title('title')

# 画图title_inside_1
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, 'b') # 'b' blue
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

# 画图title_inside_2
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g') # 注意对y进行了逆序处理     'g' green
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()