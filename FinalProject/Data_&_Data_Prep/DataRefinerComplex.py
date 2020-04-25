import csv

# cluster by age, education.num, hours worked per week
def AddRow():
    print()

with open('train_final.csv', 'r') as f:
    next(f)
    for line in f:
        lineElements = line.strip().split(',')
        if not lineElements[1] is '?' or lineElements[6] is '?' or lineElements[13] is '?':
            AddRow(lineElements)
