
heapSize = 0

def parent(i):
    return i // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2


def minHeapify(A, i):
    l = left(i)
    r = right(i)

    smallest = i

    if l < heapSize and A[l] < A[smallest]:
        smallest = l
    else:
        smallest = i

    if r < heapSize and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, smallest)

def buildMinHeap(A):
    global heapSize
    heapSize = len(A)

    for i in reversed(range(0, int(len(A) // 2))):
        minHeapify(A, i)

def minHeapSort(A):
    global heapSize
    buildMinHeap(A)

    for i in reversed(range(1, len(A))):
        A[0], A[i] = A[i], A[0]
        heapSize = heapSize - 1
        minHeapify(A, 0)