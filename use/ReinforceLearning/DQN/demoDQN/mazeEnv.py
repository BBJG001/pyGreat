# 构造gym Maze环境
import gym
from gym import spaces
import numpy as np
import time

from gym.envs.classic_control import rendering


class Maze(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    # 将会初始化动作空间与状态空间，便于强化学习算法在给定的状态空间中搜索合适的动作
    # 环境中会用的全局变量可以声明为类（self.）的变量
    def __init__(self):
        self.action_space = spaces.Discrete(5)  # 0, 1, 2，3，4: 不动，上下左右
        self.observation_space = spaces.Box(np.array([1, 1]), np.array([4, 4]), dtype=np.int)
        self.n_actions = self.action_space.n
        self.n_states = self.observation_space.shape[0] # 转态向量维度
        self.state = None
        self.target = {(4,2): 50}   # 安全/目标状态
        self.danger = {(2,2): -20, (3,3): -20}  # 危险状态

        self.viewer = rendering.Viewer(500, 500, 'maze')

    # 接收一个动作，执行这个动作
    # 用来处理状态的转换逻辑
    # 返回动作的回报、下一时刻的状态、以及是否结束当前episode及调试信息
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        x, y = self.state
        if action == 0:  # 不动
            x = x
            y = y
        elif action == 1:  # 上
            x = x
            y = y + 1
        elif action == 2:  # 下
            x = x
            y = y - 1
        elif action == 3:  # 左
            x = x - 1
            y = y
        elif action == 4:  # 右
            x = x + 1
            y = y

        next_state = np.array([x,y])
        self.state = next_state if self.observation_space.contains(next_state) else self.state

        self.counts += 1

        s = tuple(self.state)
        if s in self.danger.keys():
            reward = self.danger[s]
            done = True
        elif s in self.target.keys():
            reward = self.target[s]
            done = True
        else:
            reward = -0.5
            done = False

        return self.state, reward, done

    # 用于在每轮开始之前重置智能体的状态，把环境恢复到最开始
    def reset(self, startstate=None):
        '''
        :param startstate: (1,1)
        :return:
        '''
        if startstate==None:
            self.state = self.observation_space.sample()
        else:
            self.state = startstate
        self.counts = 0
        return self.state

    # metadata、render()、close()是与图像显示有关的，我们不涉及这一部分，感兴趣的同学可以自行编写相关内容。
    # render()绘制可视化环境的部分都写在这里
    def render(self, mode='human'):
        # 绘制网格
        for i in range(5):
            # 竖线
            self.viewer.draw_line(
                (50, 50),
                (50, 450),
                color=(0, 0, 0)
            ).add_attr(rendering.Transform((100 * i, 0)))
            # 横线
            self.viewer.draw_line(
                (50, 50), (450, 50)).add_attr(rendering.Transform((0, 100 * i)))

        # 绘制出口（安全状态）
        for state in self.target:
            self.drawrectangle2(state, color=(0, 1, 0))

        # 绘制危险区域
        for state in self.danger:
            self.drawrectangle2(state, color=(1, 0, 0))

        # 绘制当前state的位置(圆)
        size = 100
        center = (
            50 + self.state[0] * size - 0.5 * size,
            50 + self.state[1] * size - 0.5 * size)
        self.viewer.draw_circle(
            48, 30, filled=True, color=(1, 1, 0)).add_attr(rendering.Transform(center))

        return self.viewer.render(return_rgb_array=mode == 'human')

    def close(self):
        if self.viewer:
            self.viewer.close()

    def drawrectangle(self, point, width, height, **attrs):
        '''
        画矩形
        :param point: 左下角的坐标(480,320)
        :param width: 横向长度
        :param height: 竖向长度
        :param attrs: 其他参数，such as  color=(0,0,255), linewidth=5
        :return:
        '''
        points = [point,
                  (point[0] + width, point[1]),
                  (point[0] + width, point[1] + height),
                  (point[0], point[1] + height)]
        self.viewer.draw_polygon(points, **attrs)

    def drawrectangle2(self, point, **attrs):
        '''
        画一个正多边形
        :param point: 格点坐标（4，3）
        :param attrs: 其他参数，such as  color=(0,0,1), linewidth=5
        :return:
        '''
        size = 100
        center = (50 + point[0] * size - 0.5 * size, 50 + point[1] * size - 0.5 * size)
        radius = 100 / np.sqrt(2)
        res = 4
        points = []
        for i in range(res):
            ang = 2 * np.pi * (i - 0.5) / res
            points.append((np.cos(ang) * radius, np.sin(ang) * radius))

        self.viewer.draw_polygon(points, filled=True, **attrs).add_attr(rendering.Transform(center))


if __name__ == '__main__':
    env = Maze()
    for epoch in range(100):
        env.reset()
        while True:
            print(env.state)
            env.render()
            # action = env.action_space.sample()
            # print(action)
            # env.step(action)

            time.sleep(0.5)
            break
    env.close()
