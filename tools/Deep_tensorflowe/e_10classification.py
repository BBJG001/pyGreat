# ----------------classification
# prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2)+b_fc2)

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# number 1 to 10
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)   # one_hot 独热编码（源于弹幕）


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# 计算准确率
def compute_accuracy(v_xs, v_ys):
    # global prediction # 这一步没有能不能行，目测没什么问题，下面的其中的sess对象也没有这步操作，前面的RL对象也是在定义的方法中直接就用了
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.arg_max(y_pre, 1), tf.arg_max(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # 预测对了就是1，错了就是0，求平均值就是准确率
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


# 定义data_x和data_y的格式/位置（通过placeholder）
xs = tf.placeholder(tf.float32, [None, 784])  # 28*28
ys = tf.placeholder(tf.float32, [None, 10])

# 定义输出层
prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)  # softmax一般是用来做分类的，分成这种稀疏的分类结果,每个维度上都是概率值

# 定义损失函数
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))  # 交叉熵

# 定义每一轮训练的有效动作——do最优（小）化损失函数
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 定义一个产品经理（进行协同调配的）
sess = tf.Session()

# 初始化所有变量
sess.run(tf.global_variables_initializer())

for step in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  # 随机梯度下降，选一份
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
    if step % 50 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))
