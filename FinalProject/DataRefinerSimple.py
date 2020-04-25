import csv

# Insert each nonempty value of this line into the dictionaries.
def InsertIntoDictionaries(lineElements, workclassDict, occupationDict, countryDict):
    if lineElements[1] != '?':
        UpdateDict(lineElements[1], int(lineElements[14]), workclassDict)
    if lineElements[6] != '?':
        UpdateDict(lineElements[6], int(lineElements[14]), occupationDict)
    if lineElements[13] != '?':
        UpdateDict(lineElements[13], int(lineElements[14]), countryDict)

# Updates the passed in dictionary with value
def UpdateDict(value, index, dict):
    if value in dict[index]:
        dict[index][value] += 1
    else:
        dict[index][value] = 1

def CalculateLargetColumnVals(workclassDict,occupationDict,countryDict):
    mostClass50k = largestVal(workclassDict,1)
    mostOcc50k = largestVal(occupationDict,1)
    mostCountry50k = largestVal(countryDict,1)
    mostClassNot50k = largestVal(workclassDict,0)
    mostOccNot50k = largestVal(occupationDict,0)
    mostCountryNot50k = largestVal(countryDict,0)
    return mostClass50k, mostOcc50k, mostCountry50k, mostClassNot50k, mostOccNot50k, mostCountryNot50k

def largestVal(dict, is50k):
    currLargestName = ''
    currLargestVal = 0
    for key in dict[is50k]:
        if dict[is50k][key] > currLargestVal:
            currLargestName = key
            currLargestVal = dict[is50k][key]
    return currLargestName


# Step 1: insert into dictionaries so we can find keep track of which missing elements are to be used for replacement.
occupationDict = [{}, {}]
workclassDict = [{}, {}]
countryDict = [{}, {}]
with open('train_final.csv', 'r') as f:
    next(f)
    for line in f:
        lineElements = line.strip().split(',')
        InsertIntoDictionaries(lineElements, workclassDict, occupationDict, countryDict)

# Step 2: Insert into a csv file the updated values for the missing elements
with open('train_final_updated.csv', mode='w', newline='') as employee_file:
    writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('train_final.csv', 'r') as f:
        next(f)
        mostClass50k, mostOcc50k, mostCountry50k, mostClassNot50k, mostOccNot50k, mostCountryNot50k = CalculateLargetColumnVals(workclassDict,occupationDict,countryDict)
        for line in f:
            lineElements = line.strip().split(',')
            insertArr = []
            for currIter, element in enumerate(lineElements):
                is50k = int(lineElements[14])
                # If element is not in column with a potentially missing value, append to insert array.
                if currIter not in [1,6,13] or element != '?':
                    insertArr.append(element)
                else:
                    if currIter == 1:
                        if is50k == 0:
                            insertArr.append(mostClassNot50k)
                        else:
                            insertArr.append(mostClass50k)
                    elif currIter == 6:
                        if is50k == 0:
                            insertArr.append(mostOccNot50k)
                        else:
                            insertArr.append(mostOcc50k)
                    else:
                        if is50k == 0:
                            insertArr.append(mostCountryNot50k)
                        else:
                            insertArr.append(mostCountry50k)
            writer.writerow(insertArr)
print()