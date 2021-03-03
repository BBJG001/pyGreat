import tensorflow as tf

# 所有的操作生效都需要特意搞一波
# 变量的声明需要 initialize 初始化
# 操作的执行需要 run()

# tf.variable() tf声明变量
# tf.constant() tf声明常量

state = tf.Variable(0, name='counter')
print(state.name)
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init = tf.initialize_all_variables()  # must have if define variable

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
