import tensorflow as tf
import numpy as np

# ---------- 可视化tensorboard
#
# scalar标量？（比如loss）
# loss = ****
# tf.summary.scalar('loss/', loss)    # 在event中显示，看loss很重要
#
# graph框架图 && distribution分配分布？
# with tf.name_scope('x'):  # 这个scope会在显示的时候生成一个框，把这个with范围内的内容框在这个框下
#   x = jfalji(fjaoef, name = 'x_show') # 这里的name是实际显示出来的name
#
# histograms直方图/柱状图
# outputs = *****
# tf.summary.histogram(layer_name+'/outputs', outputs)
#
# tf.summary下面的一些列方法xxx('name', value)会记录一些键值，
# writer = tf.summary.FileWriter('log/', sess.graph)进行保存？


def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('Weight'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(' ', Weights)  # 这里的name参数看情况，name_scope的层级关系会构成一个层次目录
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(' ', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name+'/outputs', outputs)
        return outputs

# Make some real data
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise  # np.square()平方

with tf.name_scope('inputs'):   # scope在可视化的时候
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')  # 名字用于可视化的时候显示
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')
# 输入层x_data（size：1）; 隐层l1（size：10）; 输出层prediction（size：1）
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)  # 1输入规格，10隐层规格，relu激活函数
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_data - prediction), reduction_indices=[1]))  # 平均误差
    tf.summary.scalar('loss/', loss)    # 在event中显示，看loss很重要
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 梯度下降优化，穿一个学习率的参数（0-1）

sess = tf.Session()
merged = tf.summary.merge_all()     # 合并展示
writer = tf.summary.FileWriter('log/', sess.graph)
sess.run(tf.global_variables_initializer())

for step in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys:y_data})
    if step%50==0:
        result = sess.run(merged, feed_dict={xs:x_data, ys:y_data})
        writer.add_summary(result, step)

