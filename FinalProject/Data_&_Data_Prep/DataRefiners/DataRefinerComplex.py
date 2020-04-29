import csv
import numpy as np
import tensorflow as tf
from tensorflow import keras

"""featureNum = 84
train_data = np.genfromtxt('../trainVectorized.csv', delimiter=',')
X_train = np.delete(train_data, list(range(1,9)) + list(range(34,48)), axis=1)
y_train = train_data[:,range(1,9)]

test_data = np.genfromtxt('../testVectorized.csv', delimiter=',')
X_test = np.delete(test_data, list(range(1,9)) + list(range(34,48)), axis=1)
y_test = test_data[:,range(1,9)]

WCmodel = keras.Sequential([
    keras.layers.Flatten(input_shape=(featureNum,)),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(16, activation=tf.nn.relu),
    keras.layers.Dense(8, activation=tf.nn.sigmoid),
])

WCmodel.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])

WCmodel.fit(X_train, y_train, epochs=2, batch_size=10)


test_loss, test_acc = WCmodel.evaluate(X_test, y_test)
print('WorkClass Test accuracy:', test_acc)"""

featureNum = 92
train_data = np.genfromtxt('../trainVectorized.csv', delimiter=',')
X_train = np.delete(train_data, range(34,48), axis=1)
y_train = train_data[:,list(range(35,40))+list(range(41,43))]

test_data = np.genfromtxt('../testVectorized.csv', delimiter=',')
X_test = np.delete(test_data, range(34,48), axis=1)
y_test = test_data[:,list(range(35,40))+list(range(41,43))]

OCCmodel = keras.Sequential([
    keras.layers.Flatten(input_shape=(featureNum,)),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(7, activation=tf.nn.sigmoid),
])

OCCmodel.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])

OCCmodel.fit(X_train, y_train, epochs=4, batch_size=10)


test_loss, test_acc = OCCmodel.evaluate(X_test, y_test)
print('Occupation Test accuracy:', test_acc)

with open('../trainVectorized.csv', 'a+', newline='') as f:
    trainWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    MissingTrainVals = np.genfromtxt('../trainMissingVectorized.csv', delimiter=',')
    for rowNum in range(0,1421):
        row = []
        currRow = MissingTrainVals[rowNum:rowNum + 1]

        for index in range(0,34):
            row.append(currRow[0][index])

        prediction = OCCmodel.predict(currRow)
        largestSoFar = 0
        row.append(0)
        for index in range(0,7):
            if prediction[0][index] > largestSoFar:
                largestSoFar = prediction[0][index]
        for index in range(0, 7):
            if index == 5:
                row.append(0)
            if prediction[0][index] != largestSoFar:
                row.append(0)
            else:
                row.append(1)

        for index in range(9, 14):
            row.append(0)
        for index in range(34,92):
            row.append(currRow[0][index])

        trainWriter.writerow(row)


