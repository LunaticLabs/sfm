import tensorflow as tf
from tensorflow.losses import mean_squared_error as mse


def frame_loss(x0, x1, points):
    b, h, w, c = x0.shape

    warp_x = points[:, :, :, 0]
    warp_y = points[:, :, :, 1]

    warp_x = warp_x * tf.cast(w - 1, tf.float32)
    warp_y = warp_y * tf.cast(h - 1, tf.float32)
    warp = tf.stack([warp_x, warp_y], -1)

    x1_t = tf.contrib.resampler.resampler(x1, warp)
    return mse(x0, x1_t), x1_t


def spatial_smoothness_loss(x):
    gradients = tf.image.sobel_edges(x)
    return tf.reduce_mean(tf.square(gradients))


def forward_backward_consistency_loss(x):
    pass
