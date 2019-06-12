
def LCS(S, n, T, m):

    if n == 0 or m == 0:
        return 0
    if S[n - 1] == T[m - 1]:
        return 1 + LCS(S, n - 1, T, m - 1)
    else:
        return max(LCS(S, n - 1, T, m), LCS(S, n, T, m -1))

def LCSlength(X, Y):
    m = len(X)
    n = len(Y)

    b = [[0 for i in range(m)] for i in range(n + 1)]
    c = [[0 for i in range(m)] for i in range(n + 1)]

    for j in range(0, m):
        for i in range(0, n):
            if X[j] == Y[i]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "s"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "u"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "l"
    
    return b, c

def printLCS(b, X, i, j):
    if i == 0 or j == 0:
        if b[i][j] == "s":
            print(X[i])
        return

    if b[i][j] == "s":
        printLCS(b, X, i - 1, j - 1)
        print(X[i])
    elif b[i][j] == "u":
        printLCS(b, X, i - 1, j)
    else:
        printLCS(b, X, i, j - 1)