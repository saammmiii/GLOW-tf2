import tensorflow as tf
import math
import numpy as np
tf.random.set_seed(42)

# model parameter
SQUEEZE_FACTOR = 4
K_GLOW = 16
L_GLOW = 2
ACTIVATION = tf.nn.elu
ALPHA_S_T = 1.9  # for activation in forward/backward block not the nn... remember this will become multiplier of the input/output
KERNEL_INITIALIZER_CLOSE_ZERO = tf.random_normal_initializer(0, 1e-5)
KERNEL_INITIALIZER = tf.keras.initializers.he_normal()
# HARD_KERNEL_REGULARIZER = tf.keras.regularizers.L1L2(l1=0.03, l2=0.03)
SOFT_KERNEL_REGULARIZER = tf.keras.regularizers.l2(0.01)

# training parameters
LEARNING_RATE = 1e-4
REGULARIZER_N = 5e-5
LAMBDA_LIPSCHITZ = 1e-3
BATCH_SIZE = 16
SHUFFLE_SIZE = 10000
EPOCHS = 100000
IMG_SIZE = 28  # better to be mult of SQUEEZE_FACTOR
CHANNEL_SIZE = 1
CHECKPOINT_PATH = "./checkpoints/weights"
TENSORBOARD_LOGDIR = "./logs/GLOW"

# dataset parameters
ALPHA_BOUNDARY = 0.05

# general
TF_EPS = tf.keras.backend.epsilon()