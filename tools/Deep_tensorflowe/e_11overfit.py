# coding=gbk
# ----------- overfit
# 1.增加数据量
# 2.正则化（把f（参数）加入损失函数）
# 3.dropout正则化——神经网络中的正则化，在训练的时候， 每一轮随 机 忽略掉一些神经元和神经连接，
#   其实就是在计算完这一层的输出后，按概率随机扔掉一些值，然后再传给下一层
#   使神经网络变的不完整，这样就使得训练结果不会过分依赖于某部分特定的神经元
#
#   Wx_plus_b = tf.matmul(inputs, Weights) + biases
#   # dropout，减少原本这一层的输出的维度，保留keep_prob（一项概率值eg.80%）
#   Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)

from __future__ import print_function
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

# 输入层
digits = load_digits()
X = digits.data
y = digits.target
y = LabelBinarizer().fit_transform(y)   # 对y进行one_hot化
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)


def add_layer(inputs, in_size, out_size, layer_name, activation_function=None, ):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, )
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    # dropout，减少原本这一层的输出的维度，保留keep_prob（一项概率值eg.80%）
    Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b, )
    tf.summary.histogram(layer_name + '/outputs', outputs)  # tensroboard操作
    return outputs


# define placeholder for inputs to network
keep_prob = tf.placeholder(tf.float32)
xs = tf.placeholder(tf.float32, [None, 64])  # 8x8
ys = tf.placeholder(tf.float32, [None, 10])

# hidden layer
l1 = add_layer(xs, 64, 100, 'l1', activation_function=tf.nn.tanh)
# out layer
prediction = add_layer(l1, 50, 10, 'l2', activation_function=tf.nn.softmax)

# loss
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1]))  # loss
tf.summary.scalar('loss', cross_entropy)    # tensorboard显示
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
merged = tf.summary.merge_all()
# summary writer goes in here
train_writer = tf.summary.FileWriter("logs/train", sess.graph)
test_writer = tf.summary.FileWriter("logs/test", sess.graph)

# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
sess.run(init)

for i in range(500):
    # here to determine the keeping probability
    sess.run(train_step, feed_dict={xs: X_train, ys: y_train, keep_prob: 0.5})
    if i % 50 == 0:
        # record loss
        train_result = sess.run(merged, feed_dict={xs: X_train, ys: y_train, keep_prob: 1})
        test_result = sess.run(merged, feed_dict={xs: X_test, ys: y_test, keep_prob: 1})
        train_writer.add_summary(train_result, i)
        test_writer.add_summary(test_result, i)