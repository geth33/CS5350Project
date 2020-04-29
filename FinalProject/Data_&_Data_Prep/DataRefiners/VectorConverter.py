import csv

validVectorPositions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#validVectorPositions = [1,1,0,0,1,0,1,1,1,1,1,1,1,1]
education = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
workClass = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
maritalStatuses = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
occupation = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
relationship = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']
race = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
sex = ['Female', 'Male']
country = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']

# Find the largest values so we can do some normalization.
with open('../train.csv', 'r') as f:
    for line in f:
        lineVector = []
        lineElements = line.strip().split(',')

def InsertCategory(lineVector, currVal, currDim):
    for index in range(len(currDim)):
        if currDim[index] == currVal:
            lineVector.append(1)
        else:
            lineVector.append(0)

maxAge = 80
maxFnlwgt = 150000
maxEduNum = 16
maxCapGain = 15000
maxCapLoss = 2392
maxHoursWorked = 70
with open('../test.csv', 'r') as f:
    with open('../testVectorized.csv', mode='w', newline='') as train_file:
        trainWriter = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in f:
            lineVector = []
            lineElements = line.strip().split(',')

            if validVectorPositions[0] == 1:
                lineVector.append(int(lineElements[0])/maxAge)
            if validVectorPositions[1] == 1:
                InsertCategory(lineVector, lineElements[1], workClass)
            if validVectorPositions[2] == 1:
                lineVector.append(min(int(lineElements[2])/maxFnlwgt,1))
            if validVectorPositions[3] == 1:
                InsertCategory(lineVector, lineElements[3], education)
            if validVectorPositions[4] == 1:
                lineVector.append(min(int(lineElements[4])/maxEduNum,1))
            if validVectorPositions[5] == 1:
                InsertCategory(lineVector, lineElements[5], maritalStatuses)
            if validVectorPositions[6] == 1:
                InsertCategory(lineVector, lineElements[6], occupation)
            if validVectorPositions[7] == 1:
                InsertCategory(lineVector, lineElements[7], relationship)
            if validVectorPositions[8] == 1:
                InsertCategory(lineVector, lineElements[8], race)
            if validVectorPositions[9] == 1:
                InsertCategory(lineVector, lineElements[9], sex)
            if validVectorPositions[10] == 1:
                if int(lineElements[10]) > maxCapGain:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[11] == 1:
                if int(lineElements[11]) > maxCapLoss:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[12] == 1:
                lineVector.append(int(lineElements[12])/maxHoursWorked)
            if validVectorPositions[13] == 1:
                InsertCategory(lineVector, lineElements[13], country)
            lineVector.append(lineElements[14])
            trainWriter.writerow(lineVector)


with open('../train.csv', 'r') as f:
    with open('../trainVectorized.csv', mode='w', newline='') as train_file:
        trainWriter = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in f:
            lineVector = []
            lineElements = line.strip().split(',')

            if validVectorPositions[0] == 1:
                lineVector.append(int(lineElements[0])/maxAge)
            if validVectorPositions[1] == 1:
                InsertCategory(lineVector, lineElements[1], workClass)
            if validVectorPositions[2] == 1:
                lineVector.append(min(int(lineElements[2])/maxFnlwgt,1))
            if validVectorPositions[3] == 1:
                InsertCategory(lineVector, lineElements[3], education)
            if validVectorPositions[4] == 1:
                lineVector.append(min(int(lineElements[4])/maxEduNum,1))
            if validVectorPositions[5] == 1:
                InsertCategory(lineVector, lineElements[5], maritalStatuses)
            if validVectorPositions[6] == 1:
                InsertCategory(lineVector, lineElements[6], occupation)
            if validVectorPositions[7] == 1:
                InsertCategory(lineVector, lineElements[7], relationship)
            if validVectorPositions[8] == 1:
                InsertCategory(lineVector, lineElements[8], race)
            if validVectorPositions[9] == 1:
                InsertCategory(lineVector, lineElements[9], sex)
            if validVectorPositions[10] == 1:
                if int(lineElements[10]) > maxCapGain:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[11] == 1:
                if int(lineElements[11]) > maxCapLoss:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[12] == 1:
                lineVector.append(int(lineElements[12])/maxHoursWorked)
            if validVectorPositions[13] == 1:
                InsertCategory(lineVector, lineElements[13], country)
            lineVector.append(lineElements[14])
            trainWriter.writerow(lineVector)

validVectorPositions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# validVectorPositions = [1,1,1,0,0,1,0,1,1,1,1,1,1,1,1]
with open('../test_final.csv', 'r') as f:
    with open('../testFinalVectorized.csv', mode='w', newline='') as test_file:
        testWriter = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(f)
        for line in f:
            lineVector = []
            lineElements = line.strip().split(',')

            if validVectorPositions[1] == 1:
                lineVector.append(int(lineElements[1]) / maxAge)
            if validVectorPositions[2] == 1:
                InsertCategory(lineVector, lineElements[2], workClass)
            if validVectorPositions[3] == 1:
                lineVector.append(min(int(lineElements[3]) / maxFnlwgt, 1))
            if validVectorPositions[4] == 1:
                InsertCategory(lineVector, lineElements[4], education)
            if validVectorPositions[5] == 1:
                lineVector.append(min(int(lineElements[5]) / maxEduNum, 1))
            if validVectorPositions[6] == 1:
                InsertCategory(lineVector, lineElements[6], maritalStatuses)
            if validVectorPositions[7] == 1:
                InsertCategory(lineVector, lineElements[7], occupation)
            if validVectorPositions[8] == 1:
                InsertCategory(lineVector, lineElements[8], relationship)
            if validVectorPositions[9] == 1:
                InsertCategory(lineVector, lineElements[9], race)
            if validVectorPositions[10] == 1:
                InsertCategory(lineVector, lineElements[10], sex)
            if validVectorPositions[11] == 1:
                if int(lineElements[11]) > maxCapGain:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[12] == 1:
                if int(lineElements[12]) > maxCapLoss:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[13] == 1:
                lineVector.append(int(lineElements[13]) / maxHoursWorked)
            if validVectorPositions[14] == 1:
                InsertCategory(lineVector, lineElements[14], country)
            lineVector.append(lineElements[0])
            testWriter.writerow(lineVector)

validVectorPositions = [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1]
with open('../trainMissing.csv', 'r') as f:
    with open('../trainMissingVectorized.csv', mode='w', newline='') as train_file:
        trainWriter = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in f:
            lineVector = []
            lineElements = line.strip().split(',')

            if validVectorPositions[0] == 1:
                lineVector.append(int(lineElements[0])/maxAge)
            if validVectorPositions[1] == 1:
                InsertCategory(lineVector, lineElements[1], workClass)
            if validVectorPositions[2] == 1:
                lineVector.append(min(int(lineElements[2])/maxFnlwgt,1))
            if validVectorPositions[3] == 1:
                InsertCategory(lineVector, lineElements[3], education)
            if validVectorPositions[4] == 1:
                lineVector.append(min(int(lineElements[4])/maxEduNum,1))
            if validVectorPositions[5] == 1:
                InsertCategory(lineVector, lineElements[5], maritalStatuses)
            if validVectorPositions[6] == 1:
                InsertCategory(lineVector, lineElements[6], occupation)
            if validVectorPositions[7] == 1:
                InsertCategory(lineVector, lineElements[7], relationship)
            if validVectorPositions[8] == 1:
                InsertCategory(lineVector, lineElements[8], race)
            if validVectorPositions[9] == 1:
                InsertCategory(lineVector, lineElements[9], sex)
            if validVectorPositions[10] == 1:
                if int(lineElements[10]) > maxCapGain:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[11] == 1:
                if int(lineElements[11]) > maxCapLoss:
                    lineVector.append(1)
                else:
                    lineVector.append(0)
            if validVectorPositions[12] == 1:
                lineVector.append(int(lineElements[12])/maxHoursWorked)
            if validVectorPositions[13] == 1:
                InsertCategory(lineVector, lineElements[13], country)
            lineVector.append(lineElements[14])
            trainWriter.writerow(lineVector)
