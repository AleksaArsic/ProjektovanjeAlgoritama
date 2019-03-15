
def linearSearch(A, x):

    for i in range(0, len(A)):
        if(x == A[i]):
            return i

    return -1
