import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-100, 100, 100)
# y = -x**2*0.5 + 20*x +8000


def get_track(distance, seconds):
    '''
    :param distance: (Int)缺口离滑块的距离
    :return: (List)移动轨迹
    '''
    tracks = [0]
    offsets = [0]
    for t in np.arange(0.0, seconds, 0.1):
        offset = round((1 - (1 - t / seconds)**2)  * distance)

        # offset = round(ease_out_quart(t / seconds) * distance)
        tracks.append(offset - offsets[-1])
        offsets.append(offset)
    # return offsets, tracks
    return tracks

def get_track2(distance):
    '''
  :param distance: (Int)缺口离滑块的距离
  :return: (List)移动轨迹
  '''

    # 创建存放轨迹信息的列表
    trace = []
    # 设置加速的距离
    faster_distance = distance * (3 / 5)
    # 设置初始位置、初始速度、时间间隔
    start, v0, t = 0, 0, 0.3
    now = 0
    # 当尚未移动到终点时
    while start < distance:
        # 如果处于加速阶段
        if start < faster_distance:
            # 设置加速度为2
            a = 2
        # 如果处于减速阶段
        else:
            # 设置加速度为-3
            a = -3
        # 移动的距离公式
        move = v0 * t + 1 / 2 * a * t * t
        # 此刻速度
        v = v0 + a * t
        # 重置初速度
        v0 = v
        # 重置起点
        start += move
        # 将移动的距离加入轨迹列表
        trace.append(round(move))
        if start>distance:
            trace.append((round(distance-start)))
    # 返回轨迹信息
    return trace

y = get_track(100, 2)
y = get_track2(1000)
print(y)
plt.plot(range(len(y)), y)
plt.show()