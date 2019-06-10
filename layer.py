from keras import backend as K
import keras
import tensorflow as tf

class Pulse_coupled_layer(keras.layers.Layer):
    
    def __init__(self, **kwargs):
        super().__init__()

        self.yx = kwargs.get('yf', 0.7)
        self.af = kwargs.get('af', 0.2)
        self.vf = kwargs.get('vf', 0.1)
        self.al = kwargs.get('al', 0.2)
        self.vl = kwargs.get('vl', 0.1)
        self.at = kwargs.get('at', 0.2)
        self.vt = kwargs.get('vt', 10)
        self.bias = kwargs.get('bias', 0.2)
        self.iterations = kwargs.get('it', 40)

        self.feed = tf.Variable(0)                # F
        self.link = tf.Variable(0)                # L
        self.internal_activation = tf.Variable(0) # U
        self.threshold = tf.Variable(1)           # T
        self.activation = tf.Variable(0)          # Y

    def build(self, input_shape):
        assert isinstance(input_shape, list)
        
        self.linker_kernal = self.add_weight(
            name='linker_kernal',
            shape=(8, input_shape),
            initializer='uniform',
            trainable=True,
        )

        self.feeder_kernal = self.add_weight(
            name='feeder_kernal',
            shape=(8, input_shape),
            initializer='uniform',
            trainable=True,
        )

        super().build(input_shape)

    def call(self, x):
        for i in range(self.iterations):


    def compute_output_shape(self, input_shape):
        return input_shape