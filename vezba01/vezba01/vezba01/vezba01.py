import sys

from sumOfN import *
from sumOfQuad import *
from stringManipulation import *
from listExample import *
from dictionaryMania import *
from tupleAndList import *
from setsAndLists import *

if __name__ == "__main__":

    print("Sum of first 4 numbers: ", sumOfN(4))
    print("Sum of first 6 numbers: ", sumOfN(6))
    print("Sum of first 10 numbers: ", sumOfN(10))

    print("Sum quadrats of first 2 numbers: ", sumOfQuad(int(sys.argv[1])))

    print(stringManipulation("Aleksa", "Arsic"))

    listReverse()

    print("\n\nCount the occurence of each word in file:")
    print(dictMania())

    print("\n\nTuple Mania:")
    tupleMania()

    print("\n\nSet Mania:")
    setsMania()