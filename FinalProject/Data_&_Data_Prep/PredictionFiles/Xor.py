import csv

with open('../testSubmission.csv', mode='r', newline='') as NNSubFile:
    with open('../testSubmission2.csv', mode='r', newline='') as PercepSubFile:
        with open('../testSubmission3.csv', mode='r', newline='') as xor1SubFile:
            with open('prediction.csv', mode='r', newline='') as xor2SubFile:
                next(NNSubFile)
                next(PercepSubFile)
                next(xor1SubFile)
                next(xor2SubFile)
                with open('XorSubmission.csv', mode='w', newline='') as xor_file:
                    xorWriter = csv.writer(xor_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    xorWriter.writerow(['ID', 'Prediction'])
                    diffs = 0
                    truth0 = 0
                    truth1 = 0
                    truth2 = 0
                    truth3 = 0
                    lineNum = 0
                    for NNline in NNSubFile:
                        PercepLine = next(PercepSubFile)
                        xor1Line = next(xor1SubFile)
                        # xor2Line = next(xor2SubFile)
                        NNlineElements = NNline.strip().split(',')
                        PerceplineElements = PercepLine.strip().split(',')
                        xor1Elements = xor1Line.strip().split(',')
                        # xor2Elements = xor2Line.strip().split(',')
                        truth = int(PerceplineElements[1]) + int(NNlineElements[1]) + int(xor1Elements[1])
                        """if (int(PerceplineElements[1]) == int(NNlineElements[1])) and int(NNlineElements[1]) == int(xor1Elements[1]):
                            if truth >= 2:
                                diffs += 1
                                #print('Discontinuity #%d at ID %d, doc1 had %d while doc2 had %d' % (diffs, lineNum, int(PerceplineElements[1]), int(NNlineElements[1])))
                                print(diffs)"""
                        """if truth == 3 or truth == 0:
                            xorWriter.writerow([PerceplineElements[0], int(PerceplineElements[1])])
                        elif truth == 1:
                            xorWriter.writerow([PerceplineElements[0], 1])
                        else:
                            if int(PerceplineElements[1]) == int(NNlineElements[1]) or int(PerceplineElements[1]) == int(xor1Elements[1]):
                                xorWriter.writerow([PerceplineElements[0], int(PerceplineElements[1])])
                            else:
                                xorWriter.writerow([PerceplineElements[0], int(NNlineElements[1])])

                        if truth == 3:
                            truth3 += 1
                        elif truth == 2:
                            truth2 += 1
                        elif truth == 1:
                            truth1 += 1
                        else:
                            truth0 += 1"""

                        # if int(PerceplineElements[1]) == 1 or int(NNlineElements[1]) == 1 or int(xor1Elements[1]) == 1 or int(xor2Elements[1]):
                        """if int(PerceplineElements[1]) == 1 or int(NNlineElements[1]) == 1:
                            xorWriter.writerow([PerceplineElements[0], 1])
                        else:
                            xorWriter.writerow([PerceplineElements[0], 0])"""
                        lineNum += 1
                    print('Truth0: %d, Truth1: %d, Truth2: %d, Truth3: %d' % (truth0,truth1,truth2,truth3))
                    #print(diffs)


