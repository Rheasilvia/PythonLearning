import tensorflow as tf

#复用relu
def relu(X):
    # 封装在一个scope
    with tf.variable_scope("relu", reuse=True):
        threshold = tf.get_variable("threshold")  # resue existing variable
        w_shape = (int(X.get_shape()[1]), 1)
        w = tf.Variable(tf.random_normal(w_shape), name="weight")
        b = tf.Variable(0.0, name="bias")
        z = tf.add(tf.matmul(X, w), b)

    return tf.maximum(z, threshold, name="max")  # 共享变量


n_feature = 3
X = tf.placeholder(tf.float32, shape=(None, n_feature), name="X")
with tf.variable_scope("relu"):  # create the variable
    threshold = tf.get_variable("threshold", shape=(), initializer=tf.constant_initializer(0.0))

relus = [relu(X) for i in range(5)]
output = tf.add_n(relus, name="output")
