import sys
import random

from graphUtilities import *

if __name__ == "__main__":
    

    # Driver code (initializing graph)
    index = [1, 2, 3, 4, 5]
    data = []
    vertex = []
    graph = Graph()

    for i in range(len(index)):
        d = Data(index[i])
        data.append(d)
        vertex.append(Vertex(d, VertexColor.WHITE))

    vertex[0].addNeighbour(vertex[1])
    vertex[0].addNeighbour(vertex[4])

    vertex[1].addNeighbour(vertex[0])
    vertex[1].addNeighbour(vertex[4])
    vertex[1].addNeighbour(vertex[2])
    vertex[1].addNeighbour(vertex[3])

    vertex[2].addNeighbour(vertex[1])
    vertex[2].addNeighbour(vertex[3])

    vertex[3].addNeighbour(vertex[1])
    vertex[3].addNeighbour(vertex[4])
    vertex[3].addNeighbour(vertex[2])

    vertex[4].addNeighbour(vertex[3])
    vertex[4].addNeighbour(vertex[0])
    vertex[4].addNeighbour(vertex[1])


    for v in vertex:
        graph.addVertex(v)

    # BFS

    print("BFS Done.")
    graph.BFS(graph.graph[0])
    graph.printGraph()

    print("\n")

    print("Path from vertex: ", graph.graph[0].data.index, " to vertex:", graph.graph[2].data.index, " is trough vertices:")
    graph.printPath(graph.graph[0], graph.graph[2])

    print("Path from vertex: ", graph.graph[0].data.index, " to vertex:", graph.graph[3].data.index, " is trough vertices:")
    graph.printPath(graph.graph[0], graph.graph[3])


    # DFS
    print("\n")

    print("DFS done.")
    graph.DFS()
    graph.printGraph()