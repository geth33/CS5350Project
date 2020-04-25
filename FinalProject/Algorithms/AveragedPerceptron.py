#!/usr/bin/env python
import numpy as np

def AveragedPerceptron(csvFileName, inputVectorLength, stepSize, epochNum):
    trainData = np.genfromtxt(csvFileName, delimiter=',')
    # initialize the arrays that are central to this algorithm
    avgVector = np.zeros(inputVectorLength + 1)
    weightVector = np.zeros(inputVectorLength+1)

    for epoch in range(epochNum):
        iteration = 0
        for row in trainData:
            # convert row data into a vector for multiplication
            rowVector = []
            label = row[inputVectorLength]
            if label == 0:
                label = -1
            rowVector.append(1)
            for i in range(len(row) - 1):
                rowVector.append(row[i])
            # Calculate if current weights predicted correctly. Update accordingly.
            dotProduct = np.dot(rowVector, weightVector)
            if label * dotProduct <= 0:
                negVector = np.multiply(label, rowVector)
                negVector = np.multiply(stepSize, negVector)
                weightVector = weightVector + negVector
            # Update the average weight
            avgVector = addToAverage(avgVector, weightVector, iteration)
            iteration += 1
    return avgVector

def addToAverage(avgVector, weightVector, size):
    totalSum = np.multiply(avgVector, size)
    totalSum += weightVector
    return totalSum / (size + 1)

def TestAveragedPerceptron(csvFileName, weightVector):
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


perceptronWeight = AveragedPerceptron('train.csv', 4, .01, 10)
print("AveragedPerceptron weight vector: ", perceptronWeight)
print("Number wrong with AveragedPerception: ", TestAveragedPerceptron('test.csv', perceptronWeight))