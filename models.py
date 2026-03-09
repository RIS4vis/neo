import tensorflow as tf
from tensorflow.keras import layers, models

# Deep Neural Network (DNN) Model
class DNNModel:
    def __init__(self, input_shape):
        self.model = models.Sequential([
            layers.Flatten(input_shape=input_shape),
            layers.Dense(128, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])

    def compile(self):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Convolutional Neural Network (CNN) Model
class CNNModel:
    def __init__(self, input_shape):
        self.model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
            layers.MaxPooling2D(),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])

    def compile(self):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Long Short-Term Memory (LSTM) Model
class LSTMModel:
    def __init__(self, input_shape):
        self.model = models.Sequential([
            layers.LSTM(50, input_shape=input_shape),
            layers.Dense(10, activation='softmax')
        ])

    def compile(self):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Transformer Model
class TransformerModel:
    def __init__(self, input_shape):
        self.input = layers.Input(shape=input_shape)
        self.x = layers.MultiHeadAttention(num_heads=2, key_dim=2)(self.input, self.input)
        self.x = layers.GlobalAveragePooling1D()(self.x)
        self.x = layers.Dense(64, activation='relu')(self.x)
        self.output = layers.Dense(10, activation='softmax')(self.x)
        self.model = models.Model(inputs=self.input, outputs=self.output)

    def compile(self):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])