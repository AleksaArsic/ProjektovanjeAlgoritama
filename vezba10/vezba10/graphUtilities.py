import math

class Data:
    def __init__(self, data = None):
        self.data = data

class Vertex:
    def __init__(self, data = None):
        self.edges = [] 
        self.data = data

    def addEdge(self, edge = None):

        if isinstance(edge, Edge) and edge not in self.edges:
            self.edges.append(edge)
            self.edges.sort(key = lambda x: x.weight)
        else:
            print("Check if edge is an instance of Edge or if it already exists in the list of edges")


class Edge:
    def __init__(self, s = None, d = None, w = None):
        self.source = s
        self.destination = d
        self.weight = w

class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, vertex = None):

        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices.append(vertex)
        else:
            print("Check if vertex is instance of Vertex")

    def addEdge(self, edge = None):

        if isinstance(edge, Edge):

            v = None

            for vertex in self.vertices:
                if vertex == edge.source:
                    v = vertex
                    break

            v.addEdge(edge)

        else:
            print("Check if edge is instance of Edge")

    def printGraph(self):

        for vertex in self.vertices:

            print("Vertex: ", vertex.data.data)

            for edge in vertex.edges:
                print("\tEdge to:", edge.destination.data.data, ", weight:", edge.weight)