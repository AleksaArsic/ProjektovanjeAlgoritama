import sys 

from graphUtilities import *
from dijkstraAlgorithm import *
from bellmanFordAlgorithm import *

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