# 构造gym Maze环境
import gym
from gym import spaces
import time

from gym.envs.classic_control import rendering


class EnvLine(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    # 将会初始化动作空间与状态空间，便于强化学习算法在给定的状态空间中搜索合适的动作
    # 环境中会用的全局变量可以声明为类（self.）的变量
    def __init__(self):
        self.action_space = spaces.Discrete(3)  # 动作空间，0, 1, 2: 不动，左右
        self.observation_space = spaces.Discrete(5)     # 0,1,2,3,4：状态空间
        self.n_actions = self.action_space.n    # 动作个数
        self.state = None   # 当前状态
        self.target = 4     # 安全/目标状态

        self.viewer = rendering.Viewer(520, 200)    # 初始化一张画布

    def step(self, action):
        # 接收一个动作，执行这个动作
        # 用来处理状态的转换逻辑
        # 返回动作的回报、下一时刻的状态、以及是否结束当前episode及调试信息
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        x = self.state
        if action == 0:  # 不动
            x = x
        elif action == 1:  # 左
            x = x - 1
        elif action == 2:  # 右
            x = x + 1

        # 在这里做一下限定，如果下一个动作导致智能体越过了环境边界（即不在状态空间中），则无视这个动作
        next_state = x
        self.state = next_state if self.observation_space.contains(next_state) else self.state

        self.counts += 1

        # 如果到达了终点，给予一个回报
        # 在复杂环境中多种状态的反馈配比很重要
        if self.state == self.target:
            reward = 30
            done = True
        else:   # 如果是普通的一步，给予一个小惩罚，目的是为了减少起点到终点的总路程长度
            reward = -1
            done = False

        return self.state, reward, done

    # 用于在每轮开始之前重置智能体的状态，把环境恢复到最开始
    # 在训练的时候，可以不指定startstate，随机选择初始状态，以便能尽可能全的采集到的环境中所有状态的数据反馈
    def reset(self, startstate=None):
        if startstate==None:
            self.state = self.observation_space.sample()
        else:   # 在训练完成测试的时候，可以根据需要指定从某个状态开始
            if self.observation_space.contains(startstate):
                self.state = startstate
            else:
                self.state = self.observation_space.sample()
        self.counts = 0
        return self.state

    # render()绘制可视化环境的部分都写在这里
    def render(self, mode='human'):
        # 布置状态
        for i in range(self.observation_space.n):
            self.viewer.draw_line(
                (20, 30), (100, 30), color=(0, 0, 0)
            ).add_attr(rendering.Transform((100 * i, 0)))

        # 目标位置
        self.viewer.draw_line(
            (20, 30),
            (100, 30),
            color=(0, 1, 0),
        ).add_attr(rendering.Transform((100 * 4, 0)))

        # 绘制当前位置
        self.viewer.draw_polygon(
            [(60, 30), (80, 100), (40, 100)], color=(0, 1, 0)
        ).add_attr(rendering.Transform((100 * self.state, 0)))
        self.viewer.draw_circle(
            20, 20, True, color=(0, 1, 0)
        ).add_attr(rendering.Transform((60 + 100 * self.state, 120)))

        return self.viewer.render(return_rgb_array=mode == 'human')

    def close(self):
        if self.viewer:
            self.viewer.close()

if __name__ == '__main__':
    env = EnvLine()
    for epoch in range(5):
        env.reset()
        print('Epoch', epoch+1, ': ',end='')
        print(env.state, end='')
        env.render()    # 刷新画面
        time.sleep(0.5)
        for i in range(5):
            env.step(env.action_space.sample())     # 随机选择一个动作执行
            print(' -> ', env.state, end='')
            env.render()    # 刷新画面
            time.sleep(0.5)
        print()
    env.close()
