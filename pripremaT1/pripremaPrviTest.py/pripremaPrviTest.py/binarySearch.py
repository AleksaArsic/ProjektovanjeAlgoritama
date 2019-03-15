

def binarySearch(A, start, end, x):
    midpoint = int((start + end) / 2)

    if(end < start):
        return -1

    if(A[midpoint] > x):
        return binarySearch(A, start, midpoint - 1, x)
    elif(A[midpoint] < x):
        return binarySearch(A, midpoint + 1, end, x)
    else:
        return midpoint