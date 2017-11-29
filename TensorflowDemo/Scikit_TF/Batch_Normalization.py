import tensorflow as tf
from tensorflow.contrib.layers import batch_norm
from tensorflow.contrib.layers import fully_connected

n_inputs = 28 * 28
n_hidden1 = 300
n_hidden2 = 100
n_outputs = 10

X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")

is_training = tf.placeholder(tf.bool, shape=(), name='is_training')
bn_params = {
    'is_training': is_training,
    'decay': 0.99,
    'updates_collections': None
}

with tf.contrib.framework.arg_scope(
        [fully_connected],
        normalizer_fn=batch_norm,
        normalizer_params=bn_params):  # 第一个参数是个数组，后面的参数会传递给他
    hidden1 = fully_connected(X, n_hidden1, scope="hidden1", normalizer_fn=batch_norm, normalizer_params=bn_params)
    hidden2 = fully_connected(hidden1, n_hidden2, scope="hidden2", normalizer_fn=batch_norm,
                              normalizer_params=bn_params)
    logits = fully_connected(hidden2, n_outputs, activation_fn=None, scope="outputs", normalizer_fn=batch_norm,
                             normalizer_params=bn_params)

'''
#Gradient Clipping
threshold = 1.0
learning_rate = 0.5
loss = ...
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
grads_and_var = optimizer.compute_gradients(loss=loss)
capped_gvs = [(tf.clip_by_value(grad, -threshold, threshold), var) for grad, var in grads_and_var]
training_op = optimizer.apply_gradients(capped_gvs)
'''
