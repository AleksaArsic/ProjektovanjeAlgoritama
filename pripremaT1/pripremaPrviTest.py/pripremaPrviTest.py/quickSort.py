import random

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

def randomizedPartition(A, p, r):

    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]

    return partition(A, p, r)

def randomizedQuickSort(A, p, r):

    if p < r:
        q = randomizedPartition(A, p, r)
        randomizedQuickSort(A, p, q - 1)
        randomizedPartition(A, q + 1, r)