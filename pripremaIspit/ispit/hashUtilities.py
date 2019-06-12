import math

class hashData:
    def __init__(self, key, data):
        self.key = key
        self.literal = data

        self.next = None

    def addNeighbour(self, n):
        for neighbour in self.neighbours:
            if neighbour.literal == n.literal:
                print("Already in hash map!")
                break

        self.neighbours.append(n)


def divisionMethod(k, m):
    return k % m

def multiplicationMethod(k, m):
    return math.floor(m * ((k * (math.sqrt(5) - 1 / 2)) % 1))

def chainedHashSearch(T, k, size):
    
    key = divisionMethod(k, size)
    hData = None

    if T[key] == None:
        print("No data with the given key exists.")
    else:
        hData = T[key]

    while hData != None:
        print("data: ", hData.literal)
        hData = hData.next

    print("\n")

def chainedHashInsert(T, x, size):

    key = divisionMethod(x.key, size)

    if T[key] == None:
        T[key] = x
    else:
        hData = T[key]

        while hData.next != None:
            hData = hData.next

        hData.next = x

def chainedHashDelete(T, x, size):

    key = divisionMethod(x.key, size)

    if T[key] == None:
        print("Nothing to delete.")
    else:

        hData = T[key]
        temp = None

        if hData.literal == x.literal:
            temp = hData.next
            T[key] = temp
        else:
            while hData != None:
                if hData.next.literal == x.literal:
                    hData.next = hData.next.next
                    break





def linearProbing(k, m, i):
    return (divisionMethod(k, m) + i) % m

def hashInsert(T, k, m):

    i = 0
    j = 0
    while i != m:
        j = linearProbing(k.key, m, i)
        if T[j] == None:
            T[j] == k
            return j
        else:
            i += 1

    print("Error! Hash table overflow")

def hashSearch(T, k, m):
    
    i = 0
    j = 0
    while i != m:
        j = linearProbing(k.key, m, i)
        
        if T[j] == None:
            break

        if T[j].literal == k.literal:
            return j
        i += 1

    return None
