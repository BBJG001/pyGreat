from use.ReinforceLearning.QLearning.env import EnvLine
from use.ReinforceLearning.RL_brain import QLearning
import time
import pickle

def train():
    env = EnvLine()
    model = QLearning(
        env.action_space,
        env.target,
    )

    for episode in range(100):
        # 初始化状态
        observation = env.reset()
        env.render()

        while True:

            # 基于当前状态选择动作
            action = model.choose_action(observation)

            # 执行动作，获取回报
            observation_, reward, done = env.step(action)

            # 刷新画面
            env.render()

            # 更新Q表
            model.learn(observation, action, reward, observation_)

            # 推进状态（当前状态前移）
            observation = observation_

            # 如果达到终点，获得done=True，跳出循环
            if done:
                break
            # time.sleep(0.1)   # 延时可以提高更好的可视化效果，相对的也会减慢训练
        # time.sleep(0.5)

    # 保存一下
    with open('data/qlearning.model', 'wb') as f:
        pickle.dump(model, f)

    env.close()

def test():
    env = EnvLine()

    # 加载保存下的模型
    with open('data/qlearning.model', 'rb') as f:
        model = pickle.load(f)
    model.epsilon = 1   # 因为是测试（应用），讲epsilon设置成1，省掉“探索”的过程，直接“利用”

    for episode in range(10):
        print('episode', episode, '----------')
        for i in range(env.observation_space.n):
            print(i)
            # 初始化转态
            observation = env.reset(i)  # 遍历着在状态空间里初始化
            print('res',observation)
            env.render()
            time.sleep(1)

            while True:
                action = model.choose_action(observation)
                observation_, reward, done = env.step(action)   # 执行动作，获得下一个状态，回报
                env.render()
                observation = observation_
                if done:
                    break
                time.sleep(0.5)
            time.sleep(1)
    env.close()

if __name__ == '__main__':

    # 训练一下
    train()

    # 测试一下
    test()





