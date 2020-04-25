#!/usr/bin/env python
import numpy as np

def VotedPerceptron(csvFileName, inputVectorLength, stepSize, epochNum):
    trainData = np.genfromtxt(csvFileName, delimiter=',')
    # initialize the arrays that are central to this algorithm
    perceptronArr = []
    perceptronWeight = []
    perceptronReturnVals = []
    weightVector = np.zeros(inputVectorLength + 1)
    perceptronReturnVals.append(perceptronArr)
    perceptronReturnVals.append(perceptronWeight)
    perceptronArr.append(weightVector)
    perceptronWeight.append(0)
    m = 0

    for epoch in range(epochNum):
        iteration = 0
        for row in trainData:
            iteration += 1
            # convert row data into a vector for multiplication
            rowVector = []
            label = row[inputVectorLength]
            if label == 0:
                label = -1
            rowVector.append(1)
            for i in range(len(row) - 1):
                rowVector.append(row[i])
            # Calculate if current weights predicted correctly. Update accordingly.
            dotProduct = np.dot(rowVector, perceptronArr[m])
            if label * dotProduct <= 0:
                negVector = np.multiply(label, rowVector)
                negVector = np.multiply(stepSize, negVector)
                perceptronArr.append(perceptronArr[m] + negVector)
                m += 1
                perceptronWeight.append(0)
            else:
                perceptronWeight[m] += 1
    return perceptronReturnVals

def TestVotedPerceptron(csvFileName, vectorLength, perceptronArr,weightArr):
    testData = np.genfromtxt(csvFileName, delimiter=',')
    wrongCount = 0
    for row in testData:
        sum = 0
        # convert row data into a vector for multiplication
        rowVector = []
        label = row[vectorLength]
        if label == 0:
            label = -1
        rowVector.append(1)
        for i in range(len(row) - 1):
            rowVector.append(row[i])

        for m in range(len(perceptronArr)):
            dotProduct = np.dot(rowVector, perceptronArr[m])
            sign = 1
            if dotProduct < 0:
                sign = -1
            sum += weightArr[m] * sign
        if sum * label < 0:
            wrongCount += 1
            #print("sum: %d, label: %d" % (sum, label))
    return wrongCount


perceptronWeight = VotedPerceptron('train.csv', 4, 0.01, 10)
print("VotedPerceptron - all 260 weights and counts: ")
for index in range(0,260):
    print("%d count: %d" % (index, perceptronWeight[1][index]))
    print(perceptronWeight[0][index])
print("Number wrong with VotedPerceptron: %d" % TestVotedPerceptron('test.csv', 4, perceptronWeight[0], perceptronWeight[1]))