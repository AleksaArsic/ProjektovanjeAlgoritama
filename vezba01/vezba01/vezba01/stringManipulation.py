
def stringManipulation(firstString, secondString):
    
    tempFirst = firstString[0:3] 
    tempSecond = secondString[len(secondString) - 3: len(secondString)]

    retVal = tempFirst * 2 + tempSecond

    return retVal
