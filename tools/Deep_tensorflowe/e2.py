import tensorflow as tf
import numpy as np

# generate data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

# create tensorflow structure start
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0)) # 权重初始化，随机初始化，一行一列，也就是学习0.1
biases = tf.Variable(tf.zeros([1]))  # 偏置初始化，0，也就是学习0.3

y = Weights*x_data+biases

loss = tf.reduce_mean(tf.square(y-y_data))  # 定义损失函数，需要优化的
optimizer = tf.train.GradientDescentOptimizer(0.5)  # tf封装的优化器，不止一个，这里用这一个
train = optimizer.minimize(loss)    #

init = tf.initialize_all_variables()    # TensorFlow是一种先画龙（定义好框架/学习机制）最后点睛（初始化变量）的机制

# create tensorflow structure end

sess = tf.Session() # 建造操作平台
sess.run(init)  # 开干，训练

for step in range(201):
    sess.run(train)
    if step%20 == 0:
        print(step, sess.run(Weights), sess.run(biases))