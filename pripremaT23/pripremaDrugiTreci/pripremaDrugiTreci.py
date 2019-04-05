import sys
import random

import operator

from snippets import *
from histogram import *
from huffmanTree import *

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
    t.nodeCount += 1

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
    #print("Tree successor: ", treeSuccessor(t.root).data.number)

    print("\nTree delete -> nodes[3]: ", nodes[3].data.number)
    treeDelete(t, nodes[3])

    print("Inorder tree walk:")
    inorderTreeWalk(t.root)

    print("Node count: ", t.nodeCount)

    
    print("**********************************************************************************")
    print("\t\t\tHUFFMAN EXAMPLE (Binary Tree)")
    print("**********************************************************************************")

    print("Snippets: ")
    print(input1)
    print(input2)
    print(input3)
    print(input4)
    print(input5)

    d1 = getHistogram(input1)
    d2 = getHistogram(input2)
    d3 = getHistogram(input3)
    d4 = getHistogram(input4)
    d5 = getHistogram(input5)

    print("Histograms: ")
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d5)

    l1 = sorted(d1.items(), key = operator.itemgetter(1))
    l2 = sorted(d2.items(), key = operator.itemgetter(1))
    l3 = sorted(d3.items(), key = operator.itemgetter(1))
    l4 = sorted(d4.items(), key = operator.itemgetter(1))
    l5 = sorted(d5.items(), key = operator.itemgetter(1))

    print("Sorted lists: ")
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)

    makeHuffList(l5)

    root = makeHuffTree(l5)

    min = getMinFreqElem(root)

    #inorderHuffTreeWalk(root)

