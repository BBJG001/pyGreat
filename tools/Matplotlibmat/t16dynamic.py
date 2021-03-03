import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 6, 40)

plt.ion()   # 开启交互模型

for i in range(1000):
    # plt.cla()  # 每轮绘图清空画布
    plt.ylim(-1.5,1.5)  # y轴值的范围，如果不写定可能会造成y轴的抖动

    plt.plot(x,np.sin(x), c='red')
    plt.plot(x,np.cos(x), c='green')

    plt.draw()
    plt.pause(0.01)  # 暂停0.01s

    x=x+0.1     # 改变数据，以供下一轮画图

plt.ioff()  # 关闭交互模式

plt.pause(0)    # 出图，这种方式绘图最终画面会停止在屏幕上
# plt.show()    # 出图，这种方式绘图结束后会关闭画面