import sys
import random

from binaryClass import *
from binaryTree import *

def randomList():
    return random.sample(range(0, 20), 15)

if __name__ == "__main__":

    print("**********************************************************************************")
    print("\t\t\t\tBINARY TREE EXAMPLE")
    print("**********************************************************************************")

    A = randomList()
    nodes = []

    print("Random list: \n", A)

    t = Tree(Node(None, None, None, Data(A[0], chr(A[0] + 48))))

    for i in range(1, len(A)):
        node = Node(None, None, None, Data(A[i], chr(A[i] + 48)))
        nodes.append(node)
        treeInsert(t, node)


    print("Inorder tree walk:")
    inorderTreeWalk(t.root)

    print("Root node: ", t.root.data.number)
    print("Node count: ", t.nodeCount)
    print("Tree minimum: ", treeMinimum(t.root).data.number)
    print("Tree maximum: ", treeMaximum(t.root).data.number)
    print("Tree successor: ", treeSuccessor(t.root).data.number)

    print("\nTree delete -> nodes[3]: ", nodes[3].data.number)
    treeDelete(t, nodes[3])

    print("Inorder tree walk:")
    inorderTreeWalk(t.root)

    print("Node count: ", t.nodeCount)
