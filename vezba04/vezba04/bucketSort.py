
def bucketSorting(A):
    n = len(A)
    B = [[] for _ in range(n)]
    C = []

    for i in range(n):
        B[int(n * A[i])].append(A[i])

    for i in range(n):
        insertionSort(B[i])

    for i in range(len(B)):
        for j in range(len(B[i])):
            C.append(B[i][j])

    return C


def insertionSort(A):

    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key

