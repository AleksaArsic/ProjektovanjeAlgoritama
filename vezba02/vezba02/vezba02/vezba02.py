import sys
import random

from insertionSort import *
from bubbleSort import *
from linearSearch import *
from binarySearch import *


def randList():
    return random.sample(range(30), 10)

if __name__ == "__main__":

    l = []

    l = randList()
    print("Unsorted list: \n", l)

    insertionSort(l)
    print("Insertion sorted: \n", l)

    l = randList()
    print("Unsorted list: \n", l)

    bubbleSort(l)
    print("Bubble sorted: \n", l)

    l = randList()
    print("Unsorted list: \n", l)

    x = -1
    x = input("Enter a number from list: ")
    x = int(x)

    print("Index of", x, "is: ", linearSearch(l, x))

    l = randList()
    print("Unsorted list: \n", l)
    insertionSort(l)
    print("Insertion sorted: \n", l)

    x = -1
    x = input("Enter a number from list: ")
    x = int(x)

    print("Index of", x, "is: ", binarySearch(l, 0, len(l), x))
