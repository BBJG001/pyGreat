# gym环境类子类框架解读
import gym

class TestEnv(gym.Env):
    # 元数据，用于支持可视化的一些设定，改变渲染环境时的参数，如果不想改变设置，可以无
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    # __init__()：将会初始化动作空间与状态空间等环境所需的参量，便于强化学习算法在给定的状态空间中搜索合适的动作
    def __init__(self):
        self.action_space = None
        self.observation_space = None
        pass

    # step()：用于编写智能体与环境交互的逻辑
    # 它接受一个动作（action）的输入
    # 根据action给出下一时刻的状态（state）、当前动作的回报（reward）、探索是否结束（done）及调试帮助信息信息。
    def step(self, action):
        reward = None
        done = False
        info = {}
        return self.state, reward, done, info

    # reset()：用于在每轮开始之前重置智能体的状态
    def reset(self):
        return self.observation_space.sample()

    # render()：用来绘制画面可视化
    def render(self, mode='human'):
        return None

    # close()：用来在程序结束时清理画布
    def close(self):
        return None

if __name__ == '__main__':
    pass