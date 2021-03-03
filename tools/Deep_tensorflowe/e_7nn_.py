## 失败


import tensorflow as tf
import numpy as np

# 构造网络架构
## 获得输入层x_data,y_data;x_placeholder, y_placeholder;
## 构造若干干隐藏层
## 构造输出层 prediction=F(一波隐藏层h(x_data)), 其中F是激活函数

# 构造损失函数 loss=f(y_pre-y_data)

# 构造循环训练体 train_step=Optimizer().minimize(loss)

# 构造一个产品经理——session（用来宏观调度完成任务），开干
## sess.run(tf.initialize_all_variables())  # 初始化所有变量
## for ***｛循环训练体；every some_step save/print｝
## save/print/plot


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# 输入层
## 数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise  # np.square()平方
## placeholder框架
xs = tf.placeholder(tf.float32, [None, 1])  #
ys = tf.placeholder(tf.float32, [None, 1])

# 隐层l1（size：10）
l1 = tf.nn.relu(tf.matmul())
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # 1输入规格，10隐层规格，relu激活函数

# 输出层prediction（size：1）
prediction = add_layer(l1, 10, 1, activation_function=None)

# 损失函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_data - prediction), reduction_indices=[1]))  # 平均误差

# 循环训练体，每一轮训练的有效动作——do最优（小）化损失函数
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 梯度下降优化，穿一个学习率的参数（0-1）

# 定义一个产品经理（进行协同调配的）
sess = tf.Session()

# 所有变量初始化
init = tf.initialize_all_variables()
sess.run(init)

for step in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if step % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))  # 只要run()的操作的操作数中包括placeholder的变量，run（）中就要穿feed_dict
