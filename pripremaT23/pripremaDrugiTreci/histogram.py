
def getHistogram(A):

    d = {}

    for letter in A:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    return d
