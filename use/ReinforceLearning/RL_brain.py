import numpy as np
import pandas as pd
import torch
import time

from torch import nn

from use.ReinforceLearning.QLearning.env import EnvLine

class RL():
    def __init__(self):
        pass

    def chooseAction(self, observation):
        pass

    def learn(self, *args):
        pass

    def save(self, path):
        pass

    def saveParams(self):
        pass

    def load(self, path):
        pass

class QLearning(RL):
    def __init__(self, actions_space, target, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(QLearning, self).__init__()
        self.actions = actions_space    # 可以选择的动作空间
        self.target = target            # 目标状态（终点）
        self.lr = learning_rate         # 学习率
        self.gamma = reward_decay       # 回报衰减率
        self.epsilon = e_greedy         # 探索/利用 贪婪系数
        self.q_table =pd.DataFrame(columns=range(self.actions.n), dtype=np.float64) # Q值表

    def chooseAction(self, observation):
        self.check_state_exist(observation) # 调用这个函数的作用是检查Q值表中有无该状态，如果没有就向表中追加
        # 选择动作
        # 假设epsilon=0.9，下面的操作就是有0.9的概率按Q值表选择最优的，有0.1的概率随机选择动作
        # 随机选动作的意义就是去探索那些可能存在的之前没有发现但是更好的方案/动作/路径
        if np.random.uniform() < self.epsilon:
            # 选择最佳动作（Q值最大的动作）
            state_action = self.q_table.loc[observation, :]
            # 如果几个动作的Q值同为最大值，从中选一个
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            # 随机选择一个动作
            action = self.actions.sample()
        return action

    # 学习，主要是更新Q值
    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != self.target:   # 如果下一个状态不是终点
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()   # 这就是Q值的迭代更新公式
        else:
            q_target = r        # 下一个状态不是终点
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)     # update

    # 检查Q值表中有无状态state，如果没有就向表中追加
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # 向Q表中追加一个状态
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.q_table.columns),
                    index=self.q_table.columns,
                    name=state
                )
            )

    def save(self, path='./data/models/q_table.csv'):
        self.q_table.to_csv(path)

    def saveParams(self):
        pass

    def load(self, path='./data/models/q_table.csv'):
        self.q_table = pd.read_csv(path)

class DQN():
    def __init__(self,
                 n_states,
                 n_actions,
                 batch_size=32,
                 learning_rate=0.9,
                 epsilon=0.9,
                 gamma=0.9,
                 target_replace_iter=100,
                 memory_size=2000, ):
        # 调用类内自写函数生成网络
        self.eval_net, self.target_net = self.bulid_Net(n_states, n_actions), self.bulid_Net(n_states, n_actions)

        self.n_states = n_states
        self.n_actions = n_actions
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.gamma = gamma
        self.memory_size = memory_size
        self.taget_replace_iter = target_replace_iter
        self.learn_step_counter = 0  # for target updating
        self.memory_counter = 0  # for storing memory
        self.memory = np.zeros((self.memory_size, self.n_states * 2 + 2))  # 初始化记忆库
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(), lr=self.learning_rate)
        self.loss_func = nn.MSELoss()

    # 选择动作
    def choose_action(self, x):
        x = torch.unsqueeze(torch.FloatTensor(x), 0)
        if np.random.uniform() < self.epsilon:  # greedy概率内网络生成
            actions_value = self.eval_net.forward(x)
            action = torch.max(actions_value, 1)[1]
            action = int(action)
        else:  # （1-greedy）概率随机生成
            action = np.random.randint(0, self.n_actions)
        return action

    # 存储一步的信息到记忆库
    def store_transition(self, s, a, r, s_):
        transition = np.hstack((s, [a, r], s_))
        # 替换记忆库中的记忆
        index = self.memory_counter % self.memory_size
        self.memory[index, :] = transition
        self.memory_counter += 1

    # 学习，更新网络参数
    def learn(self):
        # 目标网络参数更新（经过self.taget_replace_iter步之后，为target_net网络更新参数）
        if self.learn_step_counter % self.taget_replace_iter == 0:
            self.target_net.load_state_dict(self.eval_net.state_dict())
        self.learn_step_counter += 1

        # 从记忆库中提取一个batch的数据
        data_size = self.memory_size if self.memory_counter>self.memory_size else self.memory_counter

        sample_index = np.random.choice(data_size, self.batch_size)
        b_memory = self.memory[sample_index, :]
        b_s = torch.FloatTensor(b_memory[:, :self.n_states])
        b_a = torch.LongTensor(b_memory[:, self.n_states:self.n_states + 1].astype(int))
        b_r = torch.FloatTensor(b_memory[:, self.n_states + 1:self.n_states + 2])
        b_s_ = torch.FloatTensor(b_memory[:, -self.n_states:])

        # 获得q_eval、q_target，计算loss
        q_eval = self.eval_net(b_s).gather(1, b_a)
        q_next = self.target_net(b_s_).detach()
        q_target = b_r + self.gamma * q_next.max(1)[0].view(self.batch_size, 1)
        loss = self.loss_func(q_eval, q_target)

        # 反向传递，更新eval网络
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    # 构建网络
    def bulid_Net(self, n_states, n_actions):
        return torch.nn.Sequential(
            torch.nn.Linear(n_states, 100),
            torch.nn.ReLU(),
            torch.nn.Linear(100, n_actions),
        )


if __name__ == '__main__':
    env = EnvLine()     # 这就是图示的画面环境
    model = QLearning(
        env.action_space,
        env.target,
    )
    # 训练
    for episode in range(100):
        # 初始化状态
        observation = env.reset()
        env.render()

        while True:
            # 基于当前状态选择动作
            action = model.chooseAction(observation)
            # 执行动作，获取回报
            observation_, reward, done = env.step(action)
            # 刷新画面
            env.render()
            # 学习，更新Q表
            model.learn(observation, action, reward, observation_)
            # 推进状态（当前状态前移）
            observation = observation_
            # 如果达到终点，获得done=True，跳出循环
            if done:
                break
            time.sleep(0.1)   # 延时可以提供更好的可视化效果，相对的也会减慢训练
        time.sleep(0.5)
    # 如果训练顺利，此时model中的q_table就已经收敛了
    print(model.q_table)
    #     0            1              2
    # 4   2.063857    - 0.008877      0.100000
    # 3   0.083175    - 0.015520      5.341192
    # 2   - 0.056166  - 0.060211      0.806275
    # 1   - 0.237123  - 0.236387      - 0.235704
    # 0   - 0.372681  - 0.372961      - 0.372209

    # 测试
    model.epsilon = 1  # 因为是测试（应用），讲epsilon设置成1，省掉“探索”的过程，直接“利用”

    for episode in range(10):
        print('episode', episode, '----------')
        for i in range(env.observation_space.n):
            print(i)
            # 初始化转态
            observation = env.reset(i)  # 遍历着在状态空间里初始化
            env.render()
            time.sleep(1)

            while True:
                action = model.choose_action(observation)
                observation_, reward, done = env.step(action)  # 执行动作，获得下一个状态，回报
                env.render()
                observation = observation_
                if done:
                    break
                time.sleep(0.5)
            time.sleep(1)