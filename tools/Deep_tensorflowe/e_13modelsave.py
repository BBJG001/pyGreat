# coding=gbk
import tensorflow as tf
import numpy as np

## save to file
## remember to define the same dtype and shape when restore
# W = tf.Variable([[1,2,3],[3,4,5]], dtype=tf.float32, name='weights')
# b = tf.Variable([[1,2,3]], dtype=tf.float32, name='biases')
#
# init = tf.global_variables_initializer()
#
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init)
#     save_path = saver.save(sess, 'my_net/save_net.ckpt')
#     print('Save to path:', save_path)


# restore variable
# redefine the same shape and same type for your variable
# 还得定义形状形同的变量接收者，名字貌似不必一样
M = tf.Variable(np.arange(6).reshape((2,3)), dtype=tf.float32, name='weights')
b = tf.Variable(np.arange(3).reshape((1,3)), dtype=tf.float32, name='biases')

# not need init step

saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, 'my_net/save_net.ckpt')
    print('weight:', sess.run(M))
    print('bisas:', sess.run(b))