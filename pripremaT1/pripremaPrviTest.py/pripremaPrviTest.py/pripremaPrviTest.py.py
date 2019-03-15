import sys
import random

from bubbleSort import *
from insertionSort import *
from linearSearch import *
from binarySearch import *
from mergeSort import mergeSort
from quickSort import randomizedQuickSort
from pythonMania import *


def randList(min, max, elements):
    return random.sample(range(min, max), elements)

if __name__ == "__main__":

    l = randList(0, 20, 10)
    print("Unsorted list:\n", l)

    bubbleSort(l)
    print("Bubble sorted:\n", l)

    l = randList(0, 20, 10)
    print("Unsorted list:\n", l)

    insertionSort(l)
    print("Insertion sorted:\n", l)

    x = int(input("Enter a number to find: "))
    index = linearSearch(l, x)

    if (index != -1):
        print("Number found at index: ", index)
    else: print("Number not in the list!")

    x = int(input("Enter a number to find: "))
    index = binarySearch(l, 0, len(l) - 1, x)

    if (index != -1):
        print("Number found at index: ", index)
    else: print("Number not in the list!")

    l = randList(0, 20, 10)
    print("Unsorted list:\n", l)

    mergeSort(l, 0, len(l) - 1)
    print("Merge sorted:\n", l)

    #l = randList(0, 20, 10)
    #print("Unsorted list:\n", l)

    #randomizedQuickSort(l, 0, len(l) - 1)
    #print("Insertion sorted:\n", l)

    print("Sum of first 5 natural numbers: ", sumOfN(5))
    print("Sum of first 3 natural squares: ", sumOfNsquares(3))
    print("Aleksa Arsic: ", stringManipulation("Aleksa", "Arsic"))
    listNoob()

    dictionaryMania()
    tupleMania()
    setMania()