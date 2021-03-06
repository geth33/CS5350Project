#!/usr/bin/env python
import numpy as np
import csv

def Perceptron(csvFileName, inputVectorLength, stepSize, epochNum):
    trainData = np.genfromtxt(csvFileName, delimiter=',')
    weightVector = np.zeros(inputVectorLength + 1)
    iteration = 0
    for epoch in range(epochNum):
        for row in trainData:
            iteration += 1
            # convert row data into a vector for multiplication
            rowVector = []
            label = row[inputVectorLength]
            if label == 0:
                label = -1
            rowVector.append(1)
            for i in range(len(row)-1):
                rowVector.append(row[i])

            # Calculate if current weights predicted correctly. Update accordingly.
            dotProduct = np.dot(rowVector, weightVector)
            if label * dotProduct <= 0:
                negVector = np.multiply(label,rowVector)
                negVector = np.multiply(stepSize, negVector)
                weightVector = weightVector + negVector
    return weightVector

def TestPerceptron(csvFileName, weightVector):
    testData = np.genfromtxt(csvFileName, delimiter=',')
    wrongCount = 0
    for row in testData:
        # convert row data into a vector for multiplication
        rowVector = []
        label = row[len(weightVector)-1]
        if label == 0:
            label = -1
        rowVector.append(1)
        for i in range(len(row) - 1):
            rowVector.append(row[i])
        dotProduct = np.dot(rowVector, weightVector)
        if label * dotProduct < 0:
            wrongCount += 1
            #print("label: %d actual:%f" % (label, dotProduct))
    return wrongCount

perceptronWeight = Perceptron('../Data_&_Data_Prep/trainVectorized.csv', 81, 0.01,10)
print("Standard Perceptron weight vector: ", perceptronWeight)
#print("Standard Perceptron wrong count:", TestPerceptron('../Data_&_Data_Prep/testVectorized.csv', perceptronWeight))

with open('../Data_&_Data_Prep/testFinalVectorized.csv', mode='r', newline='') as testFinalFile:
    with open('testSubmission.csv', mode='w', newline='') as testSubmissionFile:
        testWriter = csv.writer(testSubmissionFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        testWriter.writerow(['ID','Prediction'])
        for line in testFinalFile:
            csvRow = []
            row = line.strip().split(',')
            csvRow.append(row[len(row)-1])
            # check to see if cap gain is a good amount
            if row[37] != 1:
                rowVector = []
                rowVector.append(1)
                for i in range(len(row) - 1):
                    rowVector.append(float(row[i]))

                dotProduct = np.dot(rowVector, perceptronWeight)
                if dotProduct <= 0:
                    csvRow.append(0)
                    testWriter.writerow(csvRow)
                else:
                    csvRow.append(1)
                    testWriter.writerow(csvRow)
            else:
                csvRow.append(1)
                testWriter.writerow(csvRow)