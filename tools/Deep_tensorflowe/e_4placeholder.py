import tensorflow as tf

# 即使程序中只有一个常量tf.constant()，不断的迭代也会让计算图存储大量的常量
# 于是就有了placeholder这种机制，x = tf.placeholder(tf.float32, [数据规格])
# 它只是提供存放 量的位置，指明数据类型和数据维度，其数据在程序执行的时候再指定（通过feed_dict={x:3,,,}的方式）

input1 = tf.placeholder(tf.float32) # 通过tf.placeholder()定义形式变量
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)    # 通过形式变量描述运算流程

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1:[7.], input2:[2.]}))
    # 通过run()执行运算，通过feed_dict=传一个字典类型的参数
    # 注：这里output运算只进行了一步，在复杂操作中，output所有迭代用到的形式变量都要通过feed_dict传入值