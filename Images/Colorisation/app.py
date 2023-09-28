import numpy as np
 
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint

def rgb_2_gray(image):
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

import tensorflow_datasets as tfds
import tensorflow as tf

ds_train, ds_test = tfds.load('imagenet_resized/64x64', split=['train', 'validation'])

TRAIN_SIZE = 50000
TEST_SIZE = 10000

df_train = tfds.as_dataframe(ds_train.take(TRAIN_SIZE))
df_test = tfds.as_dataframe(ds_test.take(TEST_SIZE))

import numpy as np
x_train = []
for data in df_train.itertuples():
    a, x, y = data
    x = tf.image.resize(x, [48, 48], method='nearest')
    x = tf.cast(x, tf.uint32)
    x_train.append(x)

x_test = []
for data in df_test.itertuples():
    a, x, y = data
    x = tf.image.resize(x, [48, 48], method='nearest')
    x = tf.cast(x, tf.uint32)
    x_test.append(x)

x_train = np.array(x_train)
x_test = np.array(x_test)

x_train_gray = rgb_2_gray(x_train)
x_test_gray = rgb_2_gray(x_test)

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
 
x_train_gray = x_train_gray.astype('float32') / 255.
x_test_gray = x_test_gray.astype('float32') / 255.

input_img = Input(shape=(None, None, 1))  # None permet des dimensions variables
x = Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)

x = Conv2D(128, (3, 3), activation='relu', padding='same')(encoded)
x = UpSampling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint

batch_size = 64

reduce_lr = ReduceLROnPlateau(monitor='val_loss', 
                              factor=0.2, 
                              patience=5, 
                              min_lr=0.001)

model_checkpoint = ModelCheckpoint(filepath='meilleur_modele.h5', 
                                   monitor='val_loss', 
                                   save_best_only=True, 
                                   verbose=1)

early_stopping = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)

autoencoder.fit(x_train_gray,
                x_train,
                validation_data =(x_test_gray, x_test),
                epochs = 20,
                batch_size = batch_size,
                callbacks = [reduce_lr, model_checkpoint, early_stopping])