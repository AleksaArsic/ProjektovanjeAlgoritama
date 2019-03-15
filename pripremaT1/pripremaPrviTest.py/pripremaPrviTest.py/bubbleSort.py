
def bubbleSort(A):

    swapped = True

    while(swapped):
        swapped = False

        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]
                swapped = True
