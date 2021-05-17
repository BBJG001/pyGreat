# 用nn为DQN构造网络
import torch
import torch.nn as nn
import numpy as np
from mazeEnv import Maze    # 这是一个我自己写的环境
import time

class DQN():
    def __init__(self,
                 dim_state,
                 n_actions,
                 batch_size=32,
                 learning_rate=0.9,
                 epsilon=0.9,
                 gamma=0.9,
                 target_replace_iter=100,
                 memory_size=2000, ):
        # 调用类内自写函数生成网络
        self.eval_net, self.target_net = self.bulid_Net(dim_state, n_actions), self.bulid_Net(dim_state, n_actions)

        self.dim_state = dim_state  # 状态维度
        self.n_actions = n_actions  # 可选动作数
        self.batch_size = batch_size        # 小批量梯度下降，每个“批”的size
        self.learning_rate = learning_rate  # 学习率
        self.epsilon = epsilon  # 贪婪系数
        self.gamma = gamma      # 回报衰减率
        self.memory_size = memory_size                  # 记忆库的规格
        self.taget_replace_iter = target_replace_iter   # target网络延迟更新的间隔步数
        self.learn_step_counter = 0     # 在计算隔n步跟新的的时候用到
        self.memory_counter = 0         # 用来计算存储索引
        self.memory = np.zeros((self.memory_size, self.dim_state * 2 + 2))  # 初始化记忆库
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(), lr=self.learning_rate)    # 网络优化器
        self.loss_func = nn.MSELoss()   # 网络的损失函数

    # 选择动作
    def choose_action(self, x):
        x = torch.unsqueeze(torch.FloatTensor(x), 0)
        if np.random.uniform() < self.epsilon:  # greedy概率有eval网络生成动作
            actions_value = self.eval_net.forward(x)
            action = torch.max(actions_value, 1)[1]
            action = int(action)
        else:  # （1-greedy）概率随机选择动作
            action = np.random.randint(0, self.n_actions)
        return action

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
        b_s = torch.FloatTensor(b_memory[:, :self.dim_state])
        b_a = torch.LongTensor(b_memory[:, self.dim_state:self.dim_state + 1].astype(int))
        b_r = torch.FloatTensor(b_memory[:, self.dim_state + 1:self.dim_state + 2])
        b_s_ = torch.FloatTensor(b_memory[:, -self.dim_state:])

        # 获得q_eval、q_target，计算loss
        q_eval = self.eval_net(b_s).gather(1, b_a)
        q_next = self.target_net(b_s_).detach()
        q_target = b_r + self.gamma * q_next.max(1)[0].view(self.batch_size, 1)
        loss = self.loss_func(q_eval, q_target)

        # 反向传递，更新eval网络
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    # 存储一步的信息到记忆库
    def store_transition(self, s, a, r, s_):
        transition = np.hstack((s, [a, r], s_))
        # 存储记忆（如果第一轮存满了，就覆盖存入）
        index = self.memory_counter % self.memory_size
        self.memory[index, :] = transition
        self.memory_counter += 1

    # 构建网络
    def bulid_Net(self, dim_state, n_actions):
        return torch.nn.Sequential(
            torch.nn.Linear(dim_state, 50),
            torch.nn.ReLU(),
            torch.nn.Linear(50, n_actions),
        )

if __name__ == '__main__':
    env = Maze()
    dqn = DQN(env.n_states, env.n_actions)

    print('Collecting experience...')
    for i_episode in range(200):
        s = env.reset()                 # 重置初始状态
        ep_r = 0
        while True:
            env.render()                # 刷新画面

            a = dqn.choose_action(s)    # 选择动作
            s_, r, done = env.step(a)   # 执行动作，获得下一个状态s_，回报r，是否结束标记done
            dqn.store_transition(s, a, r, s_)   # 存储 一步 的信息
            ep_r += r                   # ep_r，一轮中的总回报
            if dqn.memory_counter > dqn.memory_size:    # 当记忆库存满（非必要等到存满）的时候，开始训练
                dqn.learn()
                if done:
                    if i_episode%20==0:
                        print('Ep: ', i_episode + 1, '| Ep_r: ', round(ep_r, 2))
            if done:                    # 如果done（智能到达终点/掉入陷阱），结束本轮
                break
            s = s_

    # 测试部分
    print('Testing . . .')
    # dqn.epsilon = 1
    rs = []
    for state in range(50): # 循环50次测一测平均回报
        s = env.reset()
        ep_r = 0
        while True:
            env.render()
            time.sleep(0.5) # 测试阶段加延时放慢可视化
            a = dqn.choose_action(s)
            s_, r, done = env.step(a)
            ep_r += r
            # 测试阶段就不再有存储和学习了
            if done:
                # print(ep_r)
                rs.append(ep_r)
                break
            s = s_

    env.close()

    # print(np.average(rs))
    # v1: -25.63
    # v2_liner: -25.21
    # v2_relu:
