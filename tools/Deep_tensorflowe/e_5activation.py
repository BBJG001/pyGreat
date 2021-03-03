import tensorflow as tf
import numpy as np

# 激活函数，一个非线性函数，以线性部分的结果为自变量，激活函数作为外层函数进行非线性化
# y = f（W（x））   其中W（x）就是线性部分的函数
# 可以自己写激励函数，必须保证激励函数是可以微分的，这样才可以保证能进行误差反向传递
# 线性可以理解为均匀的变化，激励（非线性）就是不均匀的变了，对可以让网络对某些特征反应强烈，变化快；对某些特征反应迟钝，变化慢
'''
激励函数选择： 层次比较少时，可以选择多种
            卷积网络中，多用relu
            循环神经网络中，多有relu或tanh
tf.nn.relu(features, name=None)
tf.nn.relu6(features, name=None)
tf.nn.softplus(features, name=None)
tf.nn.dropout(x, keep_prob, noise_shape=None, seed=None, name=None)
tf.nn.bias_add(value, bias, name=None)
tf.sigmoid(x, name=None)
tf.tanh(x, name=None)
'''

x = tf.Variable(np.linspace(-5, 5, 200)[:, np.newaxis])  # .np.newaxis作用为增加1个维度，x.size=(200,1)

# 激活函数可以理解为 y_=f(Wx) ,
# 为了后面更好的观察激活函数的效果， 这里令W=“1”， 即y=x
# 则y_=f(Wx)=f(x)
W = tf.Variable(np.eye(200))  # 对角矩阵
# 当传入值为5是，np.eye(5)=
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# 线性运算
y_ = tf.matmul(W, x)

# 激活
y_relu = tf.nn.relu(y_, name=None)
y_sigmoid = tf.sigmoid(y_, name=None)
y_relu6 = tf.nn.relu6(y_, name=None)
y_softplus = tf.nn.softplus(y_, name=None)
y_tanh = tf.nn.tanh(y_, name=None)
# y_softmax = tf.nn.softmax(y_)     # softmax 比较特殊, 不能直接显示, 不过他是关于概率的, 用于分类
# y_scewl = tf.nn.softmax_cross_entropy_with_logits(y_)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # print(sess.run(x))

    # 作图观察
    import matplotlib.pyplot as plt  # python 的可视化模块

    plt.figure(1, figsize=(12, 6))
    plt.subplot(231)
    # 所有的值都需要run（初始化），所有的操作都需要run（操作）
    plt.plot(sess.run(x), sess.run(y_relu), c='red', label='relu')
    plt.ylim((-1, 5))
    plt.legend(loc='best')

    plt.subplot(232)
    plt.plot(sess.run(x), sess.run(y_sigmoid), c='red', label='sigmoid')
    plt.ylim((-0.2, 1.2))
    plt.legend(loc='best')

    plt.subplot(233)
    plt.plot(sess.run(x), sess.run(y_relu6), c='red', label='relu6')
    plt.ylim((-1, 5))
    plt.legend(loc='best')

    plt.subplot(234)
    plt.plot(sess.run(x), sess.run(y_tanh), c='red', label='tanh')
    plt.ylim((-1.2, 1.2))
    plt.legend(loc='best')

    plt.subplot(235)
    plt.plot(sess.run(x), sess.run(y_softplus), c='red', label='softplus')
    plt.ylim((-0.2, 6))
    plt.legend(loc='best')

    plt.show()