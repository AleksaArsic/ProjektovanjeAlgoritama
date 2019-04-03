import sys
import time
import random

from sortingAlgorithms import *

def randomList():
    return random.sample(range(0, 20), 10)

def randomFloatList():
    return random.uniform(0, 1)

if __name__ == "__main__":

    A = randomList()

    print("Random unsorted sample: \n", A)
    begin_time = time.clock()
    maxHeap(A)
    end_time = time.clock() - begin_time
    print("Max-Heap sorted sample: \n", A)
    print("Time used for Max-Heap sort: ", end_time, "\n")

    A = randomList()
    print("Random unsorted sample: \n", A)
    begin_time = time.clock()
    minHeap(A)
    end_time = time.clock() - begin_time
    print("Min-Heap sorted sample: \n", A)
    print("Time used for Min-Heap sort: ", end_time, "\n")

    A = [randomFloatList() for _ in range(11)]
    print("Random unsorted float sample: \n", A)
    begin_time = time.clock()
    B = bucketSort(A)
    end_time = time.clock() - begin_time
    print("Bucket sorted sample: \n", B)
    print("Time used for Bucket sort: ", end_time, "\n")

    A = randomList()
    C = A
    B = [0 for _ in range(len(A))]
    print("Random unsorted sample: \n", A)
    begin_time = time.clock()
    countingSort(A, B, max(A))
    end_time = time.clock() - begin_time
    print("Counting sorted sample: \n", B)
    print("Time used for Counting sort: ", end_time, "\n")
