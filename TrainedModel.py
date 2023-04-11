import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

# load data from dataset
data = pd.read_csv("dataset.csv", delimiter=',')
# get labels
labels = data['result']
# get features
features = data.iloc[:, :-1]

# encode the categorical columns
encoders = {}
categorical_cols = ['protocol_type', 'service', 'flag']
for col in categorical_cols:
    encoder = LabelEncoder()
    encoder.fit(features[col])
    np.save(f'encoded{col.capitalize()}.nps', encoder.classes_)
    features[col] = encoder.transform(features[col])
    encoders[col] = encoder

# label encoder
labelEncoder = LabelEncoder()
labelEncoder.fit(labels)
np.save('encodedLabel.nps', labelEncoder.classes_)
encoded_Y = labelEncoder.transform(labels)
print(encoded_Y.shape)
targets = np_utils.to_categorical(encoded_Y)

# create model
model = Sequential()
model.add(Dense(45, activation='relu', input_dim=features.shape[1]))
model.add(Dense(45, activation='relu'))
model.add(Dense(targets.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(features, targets, epochs=20)

model.save('NeuralNetwork.h5')
