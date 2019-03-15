import sys

def dictMania():
    
    retVal = {}
    fin = open("dict_test.txt", 'r')
    
    for line in fin:
        words = line.split()
        for word in words:
            if word not in retVal:
                retVal[word] = 1
            else:
                retVal[word] += 1

    fin.close()

    return retVal
