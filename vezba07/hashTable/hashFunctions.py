import math

# hashSize should be defined by the user

def divisionMethod(keyVal, hashSize):
    return keyVal % hashSize

def multiplyMethod(keyVal, hashSize):
    A = (math.sqrt(5) - 1 ) / (2)
    return int((hashSize * (keyVal * A % 1)))

def doubleHashing(keyVal, hashSize):
    return ((divisionMethod(keyVal, hashSize) + multiplyMethod(keyVal, hashSize)) % hashSize)

def chainedHashInsert(list, data, hashSize):

    # insert data at the head of list T[h(data.key)]
    # check if there is a list entry at the returned index

    index = doubleHashing(data.key, hashSize)
    if list[index] == None:
        list[index] = data
    else:

        tempData = list[index]

        while tempData.next != None:
            tempData = tempData.next

        tempData.next = data

def chainedHashDelete(list, data, hashSize):
    
    index = doubleHashing(data.key, hashSize)

    if list[index] == None:
        print("No element found with the given key")
    else:

        tempData = list[index]
        temp = None

        if tempData.value == data.value:
            temp = tempData.next
            list[index] = temp
        else:
            while tempData.next.value != data.value:
                temp = tempData
                tempData = tempData.next

            temp = tempData
            temp.next = tempData.next.next

def chainedHashSearch(list, key, hashSize):
    
    index = doubleHashing(key, hashSize)
    
    if list[index] == None:
        print("No elements found with the given key.")
    else:
        printChain(list[index])

def printChain(data):

    tempData = data

    print("Chain data:")

    print(tempData.value)

    while tempData.next != None:
        print(tempData.next.value)
        tempData = tempData.next

def printChainedHash(list, hashSize):
    for i in range(0, hashSize):
        if list[i] != None:
            print("index: ", i, "data: ", list[i].value)

            tempData = list[i]

            while tempData.next != None:
                print("linked data [", i, "]:", tempData.next.value)
                tempData = tempData.next
