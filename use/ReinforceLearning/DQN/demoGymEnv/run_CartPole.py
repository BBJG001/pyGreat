import gym
from RL_DQN import DQN  # 这是我自己写的一个DQN网络

env = gym.make('CartPole-v0')   # 获得gym环境
env = env.unwrapped

print(env.action_space)
print(env.observation_space)
print(env.observation_space.low)
print(env.observation_space.high)
print(env.observation_space.shape)
print(env.observation_space.sample())
# Discrete(2)
# Box(4,)
# [-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38]
# [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38]
# (4,)
# [-4.1981392e+00  1.1287736e+38 -3.8320544e-01 -2.4842601e+38]

RL = DQN(env.observation_space.shape[0], env.action_space.n)

total_steps = 0

# 训练
for i_episode in range(2000):
    observation = env.reset()
    ep_r = 0
    while True:
        # env.render()  # 不进行可视化可以加速训练过程，取消注释可以观察训练过程
        action = RL.choose_action(observation)                          # 选择动作
        observation_, reward, done, info = env.step(action)             # 执行动作
        RL.store_transition(observation, action, reward, observation_)  # 存储 一步 的信息到记忆库
        ep_r += reward          # ep_r用来计算总回报
        if total_steps > 500:   # 待到记忆库中存有一些信息后，从里面抽取样本进行训练
            RL.learn()
        if done:                # 达到结束条件，结束本轮（跳出循环）
            if i_episode%20==0:
                print('episode: ', i_episode,
                      'ep_r: ', round(ep_r, 2),
                      )
            break

        observation = observation_  # 更新当前状态
        total_steps += 1

# 测试，测试过程中不再有学习的过程
for i_episode in range(200):
    observation = env.reset()
    ep_r = 0
    while True:
        env.render()
        action = RL.choose_action(observation)
        observation_, reward, done, info = env.step(action)
        # 这里不再有学习的过程
        ep_r += reward
        if done:
            print('episode: ', i_episode,
                  'ep_r: ', round(ep_r, 2),
                  )
            break
        observation = observation_
        total_steps += 1

env.close()

