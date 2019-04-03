
def countingSorting(A, B, k):
    
    C = [0] * (k + 1)

    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for j in reversed(range(-1, len(A))):
        B[C[A[j]] - 1] = A[j]
        C[A[j] - 1] = C[A[j]] - 1