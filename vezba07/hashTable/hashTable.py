import sys
import math
import string
import random
import time

from data import *
from hashFunctions import *

hashSize = 23
elements = 100000

def randomString(len = 8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))

def randList(max, noOfElements):
    return [random.choice(range(0, max)) for i in range(noOfElements)]

if __name__ == "__main__":


    list = [None] * hashSize
    print(list)

    l = randList(hashSize, elements)

    start_time = time.clock()
    for i in range(len(l)):
        d = Data(l[i], randomString())
        chainedHashInsert(list, d, hashSize)
    end_time = time.clock() - start_time

    print("\n")
    chainedHashSearch(list, 1, hashSize)
    print("\n")

    chainedHashDelete(list, d, hashSize)
    printChainedHash(list, hashSize)

    print("Time used for hash table with size", hashSize, " to be formed from", elements, "elements: ", end_time, "s")