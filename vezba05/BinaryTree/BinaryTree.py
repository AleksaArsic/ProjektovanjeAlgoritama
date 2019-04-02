
import sys
import random

from binaryClass import *
from binaryTreeHandler import *

def randList():
    return random.sample(range(0, 20), 10)

if __name__ == "__main__":
    A = randList()

    nodes = []

    print(A)

    T = Tree(Node(None, None, None, Data(A[0], chr(A[0] + 48))))

    for i in range(1, len(A)):
        node =  Node(None, None, None, Data(A[i], chr(A[i] + 48)))
        nodes.append(node)
        treeInsert(T,node)

    print("inorderTreeWalk: ")
    inorderTreeWalk(T.root)

    print("\n")
    print("Size of tree: ", T.nodeCount)

    print("Tree search -> treeSearch(T.root, A[3]) : ", treeSearch(T.root, A[3]).data.a1)
    print("Iterative tree search -> iterativeTreeSearch(T.root, A[3]) : ", iterativeTreeSearch(T.root, A[3]).data.a1)

    print("Tree minimum: ", treeMinimum(T.root).data.a1)
    print("Tree maximum: ", treeMaximum(T.root).data.a1)
    print("Tree successor: ", treeSuccessor(T.root).data.a1)
    print("\nTree delete -> treeDelete(nodes[3]), nodes[3] = ", nodes[3].data.a1)
    treeDelete(T, nodes[3])

    print("inorderTreeWalk: ")
    inorderTreeWalk(T.root)

    print("\n")
    print("Size of tree: ", T.nodeCount)