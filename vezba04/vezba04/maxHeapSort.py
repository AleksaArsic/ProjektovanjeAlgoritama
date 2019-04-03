
heapSize = 0

def parent(i):
    return i // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def maxHeapify(A, i):
    l = left(i)
    r = right(i)

    largest = i

    if l < heapSize and A[l] > A[largest]:
        largest = l
    else:
        largest = i

    if r < heapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)


def buildMaxHeap(A):
    global heapSize
    heapSize = len(A)

    for i in reversed(range(0, int(len(A) // 2))):
        maxHeapify(A, i)


def maxHeapSort(A):
    global heapSize
    buildMaxHeap(A)

    for i in reversed(range(1, len(A))):
        A[0], A[i] = A[i], A[0]
        heapSize = heapSize - 1
        maxHeapify(A, 0)


