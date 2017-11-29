import tensorflow as tf

# remove the previous weights and bias
tf.reset_default_graph()

save_file = './model.ckpt'

#命名报错，tf如果没有定义name,tf会自动创建一个，会吧把第一个节点命名为type，后续的命名为<type>_<number>,
# 如果不同顺序的权重和偏置会对模型产生影响，因此采用指定name避免这种问题

# two tensor variables:weights and bias
weights = tf.Variable(tf.truncated_normal([2, 3]), name='weights_0')
bias = tf.Variable(tf.truncated_normal([3]), name='bias_0')

saver = tf.train.Saver()

# print the name of weights and Bias
print('Save Weights:{}'.format(weights))
print('Save Bias:{}'.format(bias.name))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.save(sess, save_file)

# remove the previous weights and bias
tf.reset_default_graph()

# two variables:weights and bias
bias = tf.Variable(tf.truncated_normal([3]), name='bias_0')
weights = tf.Variable(tf.truncated_normal([2, 3]), name='weights_0')

saver = tf.train.Saver()

print('Load Weights:{}'.format(weights.name))
print('Load Bias:{}'.format(bias.name))

with tf.Session() as sess:
    # Load the weights and bias -ERROR
    saver.restore(sess, save_file)
