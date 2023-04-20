import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

# load data from DataSet.csv
data = pd.read_csv("DataSet.csv", delimiter=',')

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
    np.save(f'encoded{col.capitalize()}.npy', encoder.classes_)
    features[col] = encoder.transform(features[col])
    encoders[col] = encoder

# label encoder
labelEncoder = LabelEncoder()
labelEncoder.fit(labels)
np.save('encodedLabel.npy', labelEncoder.classes_)
encoded_Y = labelEncoder.transform(labels)
targets = np_utils.to_categorical(encoded_Y)

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(scaled_features, targets, test_size=0.2, random_state=42)

# create model
model = Sequential()
model.add(Dense(45, activation='relu', input_dim=scaled_features.shape[1]))
model.add(Dense(45, activation='relu'))
# softmax => sum = 1
model.add(Dense(targets.shape[1], activation='softmax'))
# adam optimizer => do not use learning rate
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# train 20 times
model.fit(X_train, y_train, epochs=20, validation_data=(X_val, y_val))

model.save('NeuralNetwork.h5')

