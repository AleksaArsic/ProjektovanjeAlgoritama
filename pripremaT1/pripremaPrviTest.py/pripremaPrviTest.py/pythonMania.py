import sys

def sumOfN(x):

    retVal = 0

    for i in range(x):
        retVal += i

    return retVal

def sumOfNsquares(x):

    retVal = 0

    for i in range(x):
        retVal += x**2

    return retVal

def stringManipulation(first, second):
    return first[0:3]*2 + second[len(second) - 3: len(second)]

def listNoob():
    l = []

    for i in range(0, 100):
        l.append(i)

    print("List reversed: \n", l[::-1])

def dictionaryMania():

    dict = {}

    fin = open("dict_test.txt", "r")

    for line in fin:
        word = line.split()

        for word in line:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1

    fin.close()

    print(dict)

def tupleMania():

    first = (3, 3.14, "pi")
    second = (6, 6.28, "2*pi")
    third = (9, 9.42, "3*pi")
    fourth = (12, 12.56, "4*pi")

    l = []
    l.append(first)
    l.append(second)
    l.append(third)
    l.append(fourth)

    print("\nTuple mania\n", l)

    l.remove(first)

    print("\n", l)

def setMania():

    first = {3, 3.14, "pi"}
    second = {6, 6.28, "2*pi"}
    third = {9, 9.42, "3*pi"}
    fourth = {12, 12.56, "4*pi"}

    l = []
    l.append(first)
    l.append(second)
    l.append(third)
    l.append(fourth)

    print("\nSet mania\n", l)

    l.remove(first)

    print("\n", l)