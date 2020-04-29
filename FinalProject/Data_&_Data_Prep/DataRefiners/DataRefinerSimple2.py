import csv

testSetStart = 15000
testSize = 1500
with open('../train.csv', mode='w', newline='') as train_file:
    with open('../test.csv', mode='w', newline='') as test_file:
        with open('../trainMissing.csv', mode='w', newline='') as trainMissing_file:
            trainWriter = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            trainMissingWriter = csv.writer(trainMissing_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            testWriter = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            with open('../train_final.csv', 'r') as f:
                next(f)
                currRow = 0
                for line in f:
                    lineElements = line.strip().split(',')
                    if lineElements[1] != '?' and lineElements[6] != '?' and lineElements[13] != '?':
                        if testSetStart <= currRow <= testSetStart + testSize:
                            testWriter.writerow(lineElements)
                        else:
                            trainWriter.writerow(lineElements)
                        currRow += 1
                    else:
                        # rather than deleting everything, we insert rows with missing values into a new file.
                        # we can delete everything by just leaving this else statement blank.
                        if lineElements[13] == '?':
                            lineElements[13] = 'United-States'
                            # Country is not super important so it's not that bad to replace 500 or so missing vals with US
                            trainWriter.writerow(lineElements)
                        else:
                            lineElements[1] = 'Private'
                            trainMissingWriter.writerow(lineElements)