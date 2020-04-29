from sklearn.ensemble import RandomForestClassifier
import numpy as np
import csv

featureNum = 105
train_data = np.genfromtxt('../Data_&_Data_Prep/trainVectorized.csv', delimiter=',')
xTrain = train_data[:,0:featureNum]
yTrain = train_data[:,featureNum]

test_data = np.genfromtxt('../Data_&_Data_Prep/testVectorized.csv', delimiter=',')
xTest = test_data[:,0:featureNum]
yTest = test_data[:,featureNum]

testFinal_data = np.genfromtxt('../Data_&_Data_Prep/testFinalVectorized.csv', delimiter=',')
X_testFinal = testFinal_data[:,0:featureNum]
test_finalIDs = testFinal_data[:,featureNum]

model = RandomForestClassifier(n_estimators=35)
model.fit(xTrain, yTrain)
print(model.score(xTest, yTest))
print()

with open('../Data_&_Data_Prep/testSubmission.csv', mode='w', newline='') as testSubmissionFile:
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