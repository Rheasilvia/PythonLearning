'''
import tensorflow as tf

# 确保不会超过上下限

v = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

with tf.Session() as sess:
    print(sess.run(tf.clip_by_value(v, 2.5, 4.5)))
'''

'''

# tf.select函数和tf.greater函数的用法
import tensorflow as tf

v1 = tf.constant([1.0, 2.0, 3.0, 4.0])
v2 = tf.constant([4.0, 3.0, 2.0, 1.0])

sess = tf.InteractiveSession()
print(sess.run(tf.greater(v1, v2)))

print(sess.run(tf.where(tf.greater(v1, v2), v1, v2)))  # 用where代替select

sess.close()
'''

# L2 损失函数
import tensorflow as tf

x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

w = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
y = tf.matmul(x, w)

weights = tf.constant([[1., -2.], [-3., 4.]])
with tf.Session() as sess:
    print(sess.run(tf.contrib.layers.l1_regularizer(.5)(weights)))