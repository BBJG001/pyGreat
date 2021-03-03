# https://www.aneasystone.com/archives/2018/03/python-selenium-geetest-crack.html
import random

import numpy as np
import math
import matplotlib.pyplot as plt


def ease_out_quad(x):
    return 1 - (1 - x) * (1 - x)


def ease_out_quart(x):
    return 1 - pow(1 - x, 4)


def ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)


# 小球落地的弹跳
def ease_out_bounce(x):
    n1 = 7.5625
    d1 = 2.75
    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        x -= 1.5 / d1
        return n1 * x * x + 0.75
    elif x < 2.5 / d1:
        x -= 2.25 / d1
        return n1 * x * x + 0.9375
    else:
        x -= 2.625 / d1
        return n1 * x * x + 0.984375


def get_track(distance, seconds):
    tracks = [0]
    offsets = [0]
    for t in np.arange(0.0, seconds, 0.1):
        offset = round(ease_out_expo(t / seconds) * distance)
        tracks.append(offset - offsets[-1])
        offsets.append(offset)
    # return offsets, tracks
    return tracks


# 一个还能划过头再回来一点儿的轨迹（未测试）
# https://blog.csdn.net/qq_39802740/article/details/83584980
def get_track7(distance):
    """
    根据偏移量和手动操作模拟计算移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    tracks = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 时间间隔
    t = 0.2
    # 初始速度
    v = 0

    while current < distance:
        if current < mid:
            a = random.uniform(2, 5)
        else:
            a = -(random.uniform(12.5, 13.5))
        v0 = v
        v = v0 + a * t
        x = v0 * t + 1 / 2 * a * t * t
        current += x

        if 0.6 < current - distance < 1:
            x = x - 0.53
            tracks.append(round(x, 2))

        elif 1 < current - distance < 1.5:
            x = x - 1.4
            tracks.append(round(x, 2))
        elif 1.5 < current - distance < 3:
            x = x - 1.8
            tracks.append(round(x, 2))

        else:
            tracks.append(round(x, 2))

    print(tracks, sum(tracks))
    return tracks


if __name__ == '__main__':
    track = get_track(100, 3)
    plt.plot(range(len(track)), track)
    plt.show()
