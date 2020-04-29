import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import csv

featureNum = 105
train_data = np.genfromtxt('../Data_&_Data_Prep/trainVectorized.csv', delimiter=',')
X_train = train_data[:,0:featureNum]
y_train = train_data[:,featureNum]

test_data = np.genfromtxt('../Data_&_Data_Prep/testVectorized.csv', delimiter=',')
X_test = test_data[:,0:featureNum]
y_test = test_data[:,featureNum]

testFinal_data = np.genfromtxt('../Data_&_Data_Prep/testFinalVectorized.csv', delimiter=',')
X_testFinal = testFinal_data[:,0:featureNum]
test_finalIDs = testFinal_data[:,featureNum]

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(featureNum,)),
    keras.layers.Dense(64, activation=tf.nn.relu),
	keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(16, activation=tf.nn.relu),
    keras.layers.Dense(8, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.sigmoid),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=2, batch_size=10)


test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)

with open('../Data_&_Data_Prep/testSubmission2.csv', mode='w', newline='') as testSubmissionFile:
    testWriter = csv.writer(testSubmissionFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    testWriter.writerow(['ID', 'Prediction'])
    rowNum = 0
    for row in X_testFinal:
        prediction = model.predict(X_testFinal[rowNum:rowNum+1])
        if prediction > 0.5:
            testWriter.writerow([rowNum+1, 1])
        else:
            testWriter.writerow([rowNum+1, 0])
        rowNum += 1