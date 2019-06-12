import sys 

from graphUtilities import *
from dijkstraAlgorithm import *
from bellmanFordAlgorithm import *
from hashUtilities import *
from lCommonSubsequence import *

hashSize = 10

if __name__ == "__main__":

    graph = Graph()

    v1 = Vertex(Data('s'))
    v2 = Vertex(Data('t'))
    v3 = Vertex(Data('y'))
    v4 = Vertex(Data('z'))
    v5 = Vertex(Data('x'))

    graph.addVertex(v1)
    graph.addVertex(v2)
    graph.addVertex(v3)
    graph.addVertex(v4)
    graph.addVertex(v5)

    graph.addEdge(Edge(v1, v2, 10))
    graph.addEdge(Edge(v1, v3, 5))

    graph.addEdge(Edge(v2, v5, 1))
    graph.addEdge(Edge(v2, v3, 2))

    graph.addEdge(Edge(v3, v2, 3))
    graph.addEdge(Edge(v3, v5, 9))
    graph.addEdge(Edge(v3, v4, 2))

    graph.addEdge(Edge(v4, v1, 7))
    graph.addEdge(Edge(v4, v5, 6))

    graph.addEdge(Edge(v5, v4, 4))

    #dijkstraAlgorithm(graph, v1)

    bellmanFordAlgortihm(graph, v1)

    graph.printGraph()

    graph.BFS(v1)
    print("\nPath from: ", v1.d.d, " to: ", v5.d.d)

    graph.printBFSpath(v1, v5)


    print("\nDFS and topological sort:")
    graph.DFS()

    for v in graph.topologicalSort:
        print("Vertex: ", v.d.d, " discovered time: ", v.disc, " finish time: ", v.finish)

    hashList = [None] * hashSize

    h1 = hashData(1, 'a')
    h2 = hashData(2, 'b')
    h3 = hashData(3, 'c')
    h4 = hashData(4, 'd')
    h5 = hashData(2, 'e')
    h6 = hashData(2, 'f')
    h7 = hashData(7, 'g')
    h8 = hashData(8, 'h')
    h9 = hashData(9, 'i')
    h10 = hashData(10, 'j')

    hList = hashList.copy()

    chainedHashInsert(hashList, h1, hashSize)
    chainedHashInsert(hashList, h2, hashSize)
    chainedHashInsert(hashList, h3, hashSize)
    chainedHashInsert(hashList, h4, hashSize)
    chainedHashInsert(hashList, h5, hashSize)
    chainedHashInsert(hashList, h6, hashSize)
    chainedHashInsert(hashList, h7, hashSize)
    chainedHashInsert(hashList, h8, hashSize)
    chainedHashInsert(hashList, h9, hashSize)
    chainedHashInsert(hashList, h10, hashSize)

    chainedHashDelete(hashList, h5, hashSize)

    chainedHashSearch(hashList, 1, hashSize)
    chainedHashSearch(hashList, 2, hashSize)
    chainedHashSearch(hashList, 3, hashSize)
    chainedHashSearch(hashList, 4, hashSize)
    chainedHashSearch(hashList, 5, hashSize)
    chainedHashSearch(hashList, 6, hashSize)
    chainedHashSearch(hashList, 7, hashSize)
    chainedHashSearch(hashList, 8, hashSize)
    chainedHashSearch(hashList, 9, hashSize)
    chainedHashSearch(hashList, 10, hashSize)

    hashInsert(hList, h1, hashSize)
    hashInsert(hList, h2, hashSize)
    hashInsert(hList, h3, hashSize)
    hashInsert(hList, h4, hashSize)
    hashInsert(hList, h5, hashSize)
    hashInsert(hList, h6, hashSize)
    hashInsert(hList, h7, hashSize)
    hashInsert(hList, h8, hashSize)
    hashInsert(hList, h9, hashSize)
    hashInsert(hList, h10, hashSize)

    print(hashSearch(hashList, h1, hashSize))
    print(hashSearch(hashList, h2, hashSize))
    print(hashSearch(hashList, h3, hashSize))
    print(hashSearch(hashList, h4, hashSize))
    print(hashSearch(hashList, h5, hashSize))
    print(hashSearch(hashList, h6, hashSize))
    print(hashSearch(hashList, h7, hashSize))
    print(hashSearch(hashList, h8, hashSize))
    print(hashSearch(hashList, h9, hashSize))
    print(hashSearch(hashList, h10, hashSize))


    stringA = "bdcaba"
    stringB = "abcbdab"

    print("Recursive lcs of", stringA, " and", stringB, " is:", LCS(stringA, len(stringA), stringB, len(stringB)))

    b, c = LCSlength(stringA, stringB)

    for i in range(len(stringA) + 1):
        print(c[i])

    print("\n")

    for i in range(len(stringA) + 1):
        print(b[i])

    printLCS(b, stringB, len(stringB) - 1, len(stringA) - 1)