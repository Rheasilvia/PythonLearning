import tensorflow as tf

# Remove the previous weights and bias
tf.reset_default_graph()

save_file = './model.ckpt'

weights = tf.Variable(tf.truncated_normal([2, 3]))
bias = tf.Variable(tf.truncated_normal([3]))

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, save_file)

    print('Weight:')
    print(sess.run(weights))
    print('Bias:')
    print(sess.run(bias))
