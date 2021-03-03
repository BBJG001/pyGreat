# 构造gym Maze环境
import gym
from gym import spaces
from gym.envs.classic_control import rendering
import time

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

        self.viewer = rendering.Viewer(520, 200)

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

        next_state = x
        self.state = next_state if self.observation_space.contains(next_state) else self.state

        self.counts += 1

        if self.state == self.target:
            reward = 30
            done = True
        else:
            reward = -1
            done = False

        return self.state, reward, done

    # 用于在每轮开始之前重置智能体的状态，把环境恢复到最开始
    def reset(self, state=None):
        if state==None:
            self.state = self.observation_space.sample()
        else:
            if self.observation_space.contains(state):
                self.state = state
            else:
                self.state = self.observation_space.sample()
        self.counts = 0
        return self.state

    # metadata、render()、close()是与图像显示有关的，我们不涉及这一部分，感兴趣的同学可以自行编写相关内容。
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
    for epoch in range(10):
        env.reset()
        print('Epoch', epoch+1, '---------------------')
        for i in range(5):
            print(env.state)
            env.render()
            env.state = env.action_space.sample()
            time.sleep(0.5)
    env.close()
