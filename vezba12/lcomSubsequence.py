
# S - string 1
# n - len(S)
# T - string 2
# m - len(s)
def LCS(S, n, T, m):
    if n == 0 or m == 0:
        return 0
    if S[n - 1] == T[m - 1]:
        return 1 + LCS(S, n - 1, T, m - 1)
    else:
        return max(LCS(S, n - 1, T, m), LCS(S, n, T, m - 1))

# X - first shorter string
# Y - second longer string
def LCSLength(X, Y):
    
    m, n = len(X), len(Y)

    b = [[0 for i in range(m + 1)] for k in range(n + 1)]
    c = [[0 for i in range(m + 1)] for k in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[j - 1] == Y[i - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "s"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "u"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "l"

    return b, c

# b - pointer array
# X - longer string
# i - length of longer string
# j - length of shorter string
def printLCS(b, X, i, j):
    if i == 0 or j == 0:
        return

    if b[i][j] == "s":
        printLCS(b, X, i - 1, j - 1)
        print(X[i - 1])
    elif b[i][j] == "u":
        printLCS(b, X, i - 1, j)
    else:
        printLCS(b, X, i, j - 1)