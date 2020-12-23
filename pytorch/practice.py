import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.math import argmax

import numpy as np

idx2char=['h','i','e','l','o']

#원핫벡터는 희소벡터
x_data=[[0, 1, 0, 2, 3, 3]]
t_data=[[1, 0, 2, 3, 2, 4]]


model=Sequential()
model.add(SimpleRNN(units=64, activation='tanh', return_sequences=True, input_shape=[6,1]))
model.add(Dense(5, activation='softmax'))

#sparse_categorical_crossentropy 다중클래스분류로 원 핫 인코딩 필요없이 정수인코딩상태에서가능
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()

hist=model.fit(x_data, t_data, epochs=100, verbose=1)

model.predict(x_data)
result=argmax(model.predict(x_data), 2)
print(result)
result_str=[idx2char[i] for i in np.squeeze(result)]
print(result_str)