import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

'''
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros(1, out_size)+0.1)
    Wx_plus_b = tf.matmul(inputs, Weights)+biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
'''


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise  # np.square()平方

xs = tf.placeholder(tf.float32, [None, 1])  #
ys = tf.placeholder(tf.float32, [None, 1])
# 输入层x_data（size：1）; 隐层l1（size：10）; 输出层prediction（size：1）
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # 1输入规格，10隐层规格，relu激活函数
prediction = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_data - prediction), reduction_indices=[1]))  # 平均误差

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 梯度下降优化，穿一个学习率的参数（0-1）

init = tf.initialize_all_variables()  # 所有变量初始化
sess = tf.Session()
sess.run(init)

# 显示真实数据
fig = plt.figure()  # 画个框
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)  # 画离散的
plt.ion()   # plt能动态画图的关键 关键 关键
# plt.show()  # show()了之后，会把画面停住，用上一行语句然plt取消‘停住’


for step in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if step % 50 == 0:
        # print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))  # 只要run()的操作的操作数中包括placeholder的变量，run（）中就要穿feed_dict
        # 画图
        try:
            # pass
            ax.lines.remove(lines[0])       # 莫大推荐先清除上一轮花的线，再重新画这一次的，效果好一些，但是第一轮没有“上一轮”，就try catch一下，在第一轮pass
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data})  # 获得y_predict
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)   # 画连续的
        # ax.lines.remove(lines[0])
        plt.pause(0.2)      # 暂停0.1继续

# 下面两步实现把画面停在桌面上，而不是一闪而过（注：这样同时是相当于停住了程序的运行）
plt.ioff()
plt.show()      # 放在最后可以把画面停住