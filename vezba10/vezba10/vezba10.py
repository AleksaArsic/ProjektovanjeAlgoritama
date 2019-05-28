import sys

from graphUtilities import *

if __name__ == "__main__":

    graph = Graph()

    # Vertices 
    v1 = Vertex(Data('s'))
    v2 = Vertex(Data('t'))
    v3 = Vertex(Data('y'))
    v4 = Vertex(Data('x'))
    v5 = Vertex(Data('z'))

    # Add vertices to graph
    graph.addVertex(v1)
    graph.addVertex(v2)
    graph.addVertex(v3)
    graph.addVertex(v4)
    graph.addVertex(v5)

    # Edges
    e1 = Edge(v1, v2, 10)
    e2 = Edge(v1, v3, 5)

    e3 = Edge(v2, v3, 2)
    e4 = Edge(v2, v4, 1)

    e5 = Edge(v3, v2, 3)
    e6 = Edge(v3, v4, 9)
    e7 = Edge(v3, v5, 2)

    e8 = Edge(v4, v5, 4)

    e9 = Edge(v5, v1, 7)
    e10 = Edge(v5, v4, 6)

    # Add edges to graph
    graph.addEdge(e1)
    graph.addEdge(e2)
    graph.addEdge(e3)
    graph.addEdge(e4)
    graph.addEdge(e5)
    graph.addEdge(e6)
    graph.addEdge(e7)
    graph.addEdge(e8)
    graph.addEdge(e9)
    graph.addEdge(e10)

    # Print graph
    graph.printGraph()
