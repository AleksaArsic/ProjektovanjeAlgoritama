
def bubbleSort(A):

    swapped = True

    while swapped:
        swapped = False

        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
                swapped = True