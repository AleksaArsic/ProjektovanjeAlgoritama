from huffmanClass import *


def makeHuffList(l):

    for i in range(len(l)):
        hNode = huffNode(None, None, None, l[i][1], l[i][0])
        l[i] = hNode

def makeNewElem(l, freq, char):

    hNode = huffNode(None, None, None, freq, char)

    for i in range(len(l)):
        if l[i].freq >= hNode.freq:
            l.insert(i, hNode)
            break

def makeHuffTree(l):

    while len(l) > 1:
        hNodeA = l.pop(0)
        hNodeB = l.pop(0)

        hNode = huffNode(hNodeA, hNodeB, None, hNodeA.freq + hNodeB.freq, None)
        hNodeA.parent = hNode
        hNodeB.parent = hNode

        if len(l) == 0:
            l.append(hNode)
        else:
            i = 0
            while l[i].freq < hNode.freq:
                i += 1
                if i == len(l):
                    break

            l.insert(i, hNode)
                

            for i in range(len(l)):
                print(l[i].freq, l[i].char)

            print("\n")
    return l[0]

def inorderHuffTreeWalk(x):
    if x != None:
        path = ""
        inorderHuffTreeWalk(x.left)
        print(x.freq, x.char, x.path)
        inorderHuffTreeWalk(x.right)

def getMinFreqElem(x):
    
    # TO-DO:

    return x

def huffmanCode(x, data):

    # TO-DO:

    huffCode = ""


   




