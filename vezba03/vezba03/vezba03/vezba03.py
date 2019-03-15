import sys
import random

from mergeSort import mergeSort
from quickSort import randomizedQuicksort

def randomList():
    return random.sample(range(100), 15)

if __name__ == "__main__":

    l = randomList()
    print("Unsorted list:\n", l)

    mergeSort(l, 0, len(l) - 1)
    print("Merge sorted: \n", l)

    l = randomList()
    print("\nUnsorted list:\n", l)

    randomizedQuicksort(l, 0, len(l) - 1)
    print("Quick sorted: \n", l)