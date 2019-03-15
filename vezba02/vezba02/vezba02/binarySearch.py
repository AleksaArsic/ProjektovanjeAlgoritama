

def binarySearch(A, start, end, x):

    midpoint = (start + end)//2

    if A[midpoint] > x:
        print(A)
        return binarySearch(A, start, midpoint - 1, x)
    elif A[midpoint] < x:
        print(A)
        return binarySearch(A, midpoint + 1, end, x)    
    else:
        print(A)
        return midpoint