import sys

from graphUtilities import *
from dijkstraAlgorithm import *
from bellmanFordAlgorithm import *

graph = None

def newShortestPath():

    bellmanFordAlgorithm(graph, graph.vertices[0])

    shortest = []
    node = graph.vertices[len(graph.vertices) - 1]

    while node.pi != None:
        shortest.append(node.pi)
        node = node.pi

    shortest.reverse()

    return shortest

def makeGraph():
    global graph
    graph = Graph()

    d = 'a'

    for i in range(7):
        v = Vertex(Data(d))
        graph.addVertex(v)
        d = chr(ord(d) + 1)


    e = Edge(graph.vertices[0], graph.vertices[1], 8)
    e1 = Edge(graph.vertices[0], graph.vertices[2], 6)

    e2 = Edge(graph.vertices[1], graph.vertices[3], 10)

    e3 = Edge(graph.vertices[2], graph.vertices[3], 15)
    e4 = Edge(graph.vertices[2], graph.vertices[4], 9)

    e5 = Edge(graph.vertices[3], graph.vertices[4], 14)   
    e6 = Edge(graph.vertices[3], graph.vertices[5], 4)   

    e7 = Edge(graph.vertices[4], graph.vertices[5], 13)    
    e8 = Edge(graph.vertices[4], graph.vertices[6], 17)    

    e9 = Edge(graph.vertices[5], graph.vertices[6], 7)    

    graph.addEdge(e)
    graph.addEdge(e1)
    graph.addEdge(e2)
    graph.addEdge(e3)
    graph.addEdge(e4)
    graph.addEdge(e5)
    graph.addEdge(e6)
    graph.addEdge(e7)
    graph.addEdge(e8)
    graph.addEdge(e9)

    return graph


if __name__ == "__main__":

    graph = makeGraph()

    graph.printGraph()

    print("\n")
    outDegrees = getOutDegrees(graph)
    print("Out degrees: \n", outDegrees)

    print("\n")
    inDegrees = getInDegrees(graph)
    print("In degrees: \n", inDegrees)

    print("\n")
    #updateEdge(graph, graph.vertices[0], graph.vertices[1], 3)

    print("\n")
    print("Dijkstra algorithm")
    dijkstraAlgorithm(graph, graph.vertices[0])
    graph.printGraph()

    shortest = shortestPath(graph, graph.vertices[0], graph.vertices[len(graph.vertices) - 1])

    print("Shortest path from vertex a to vertex g")
    for v in shortest:
        print(v.d.data)

    updateEdge(graph, graph.vertices[1], graph.vertices[2], -4)
    graph.printGraph()

    print("Bellman-Ford Algorithm")
    shortest = newShortestPath()
    graph.printGraph()

    print("Shortest path from vertex a to vertex g")
    for v in shortest:
        print(v.d.data)
