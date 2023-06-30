#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 12:01
# @Author  : FywOo02
# @FileName: Training_Model.py.py
# @Software: PyCharm

import os
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from tensorflow.python.keras.utils.np_utils import to_categorical
from matplotlib import pyplot as plt

# global variable
batch_size = 300
# from 0 to 9, total 10 numbers
num_size = 10
# number of iterations
epochs = 10
# input is a 28*28 grayscale map
img_rows, img_cols = 28, 28

###############################################    data processing   ###############################################

# load data
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# reformat the data
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1).astype('float32')

# Normalize the data
X_train_normalize = X_train / 255.0
X_test_normalize = X_test / 255.0

'''
print('X_train_Normalize shape:', X_train_normalize.shape)
print(X_train_normalize.shape[0], 'train samples')
print(X_test_normalize.shape[0], 'test samples')
'''

# convert y to hot-dot
y_test_hotdot = to_categorical(y_test, num_size)
y_train_hotdot = to_categorical(y_train, num_size)

###############################################    construct  ###############################################

# construct the feature extraction part
model = Sequential()

# first CONV
model.add(Conv2D(filters=16, kernel_size=(5, 5), padding='same', activation='relu', input_shape=(28, 28, 1)))

# first POOL
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# second CONV
model.add(Conv2D(filters=32, kernel_size=(5, 5), padding='same', activation='relu'))

# second POOL
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# third CONV
model.add(Conv2D(filters=64, kernel_size=(5, 5), padding='same', activation='relu'))

# forth CONV
model.add(Conv2D(filters=128, kernel_size=(5, 5), padding='same', activation='relu'))

# third POOL
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# flat the graph
model.add(Flatten())
# FC
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.25))

# activation function - 'softmax'
model.add(Dense(num_size, activation='softmax'))

###############################################    train   ###############################################

# train the data
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# record current train
checkpoint_save_path = "./checkpoint/mnist.ckpt"
if os.path.exists(checkpoint_save_path + '.index'):
    print('-------------load the model-----------------')
    model.load_weights(checkpoint_save_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                 save_weights_only=True,
                                                 save_best_only=True)

history = model.fit(x=X_train_normalize, y=y_train_hotdot, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(X_test_normalize, y_test_hotdot), validation_freq=1, callbacks=[cp_callback])
model.summary()

# get the result
score = model.evaluate(X_test_normalize, y_test_hotdot)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

print(model.trainable_variables)
file = open('./weights.txt', 'w')
for v in model.trainable_variables:
    file.write(str(v.name) + '\n')
    file.write(str(v.shape) + '\n')
    file.write(str(v.numpy()) + '\n')
file.close()

# save the model to local
model.save('E:\Computer Science\hand_written_digits_recognition\model.h5')

###############################################    show   ###############################################

# show the accuracy and loss curves of training and test sets
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.subplot(1, 2, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()
