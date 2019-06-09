import sys 

from lcomSubsequence import *

if __name__ == "__main__":
    stringA = "babce"
    stringB = "abdace"

    b, c = [], []

    lcs = LCS(stringA, len(stringA), stringB, len(stringB))

    print("Recursive lcs of", stringA, " and", stringB, " is:", lcs)

    b, c = LCSLength(stringA, stringB)

    b = list(b)
    c = list(c)

    for i in range(len(stringB) + 1):
        print(c[i])

    print("\n")

    for i in range(len(stringB) + 1):
        print(b[i])

    print("\n")
    printLCS(b, stringB, len(stringB), len(stringA))
