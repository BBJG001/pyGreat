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
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))    # 初始化该层中的权重矩阵W
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)     # 初始化该层中的偏置b
    Wx_plus_b = tf.matmul(inputs, Weights) + biases     # y_=Wx+b

    # 不激活的情况下，直接输出线性结果
    if activation_function is None:
        outputs = Wx_plus_b
    # 有激活函数的情况，用激活函数进行激活（非线性化）
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs, Weights, biases
    # 为了能对W和b进行输出，我在返回值中添加了W和b，实际运用中一般不会需要输出中间的W和b

# 输入层
## 数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise  # np.square()平方
## placeholder框架
xs = tf.placeholder(tf.float32, [None, 1])  # 变量容器，相当于函数中的形参，只是为了完整的描述操作流程，并不会分配内存空间
ys = tf.placeholder(tf.float32, [None, 1])

# 隐层l1（size：10）
l1 = add_layer(xs, 1, 5, activation_function=tf.nn.relu)[0]  # 1输入规格，10隐层规格，relu激活函数

# 输出层prediction（size：1）
prediction = add_layer(l1, 5, 1, activation_function=None)[0]

# 损失函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_data - prediction), reduction_indices=[1]))  # 平均误差
# 平均误差，就是 loss=y_预测-y_实际

# 循环训练体，每一轮训练的有效动作——do 最优（小）化损失函数
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# 梯度下降优化，传一个学习率的参数（0-1），每次优化的步伐大小

# 定义一个产品经理Session（进行协同调配的）
with tf.Session() as sess:

    # 所有变量初始化
    init = tf.initialize_all_variables()
    sess.run(init)

    # 训练1000次，就是不断优化W和b，使loss最小化
    for step in range(1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        # 每400步，输出一下loss，查看一下学习的权重矩阵W和偏置b
        # 为了减少输出，我这里设置了400，如果想更细的观察变化，可以减小该值
        if step % 400 == 0:
            print('loss:', sess.run(loss, feed_dict={xs: x_data, ys: y_data}))  # 只要run()的操作的操作数中包括placeholder的变量，run（）中就要穿feed_dict
            resl1 = sess.run(l1, feed_dict={xs: x_data, ys: y_data})
            respre = sess.run(prediction, feed_dict={xs: x_data, ys: y_data})
            print('l1_Weights=\n', resl1[1])
            print('l1_biases=\n', resl1[2])
            print('pre_Weights=\n', respre[1])
            print('pre_biases=\n', respre[2])
            print()
