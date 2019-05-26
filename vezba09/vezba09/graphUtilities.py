from enum import Enum
import math

class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255


class Vertex:

    def __init__(self, d = None, color = VertexColor.WHITE):
        self.data = d
        self.neighbours = []

        # BFS parameters
        self.color = color
        self.distance = math.inf
        self.pi = None

        #DFS parameters (including colorfrom BFS parameters)
        self.time = 0
        self.finish = 0

    def addNeighbour(self, d = None):

        # Could be implemented better

        if not isinstance(d, Vertex):
            print("Error!")
        else:
            self.neighbours.append(d)
            self.neighbours.sort(key = lambda x: x.data.index)

class Data:

    def __init__(self, i):
        self.index = i

class Graph:

    def __init__(self):
        self.graph = []
        self.time = 0
        self.topologicalSort = []

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.graph:
            self.graph.append(vertex)
        else:
            print("Error! Vertex is a part of the graph!")

    def printGraph(self):
        i = 0

        for v in self.graph:
            print("Vertex[", v.data.index, "]")

            print("\tList of neighbours:")
            for neighbour in v.neighbours:
                print("\t[", neighbour.data.index, "]:", neighbour.color, ", dist:", neighbour.distance, ", time:", neighbour.time, ", finish: ", neighbour.finish)

            i += 1

    def BFS(self, start):
        
        for vertex in self.graph:
            vertex.color = VertexColor.WHITE
            vertex.pi = None

        q = []

        if not isinstance(start, Vertex):
            print("Error! Start point must be Vertex!")
        else:

            start.color = VertexColor.GRAY
            start.distance = 0
            start.pi = None

            q.append(start)

            while len(q) > 0:
                u = q.pop(0)

                for vertex in u.neighbours:
                    if vertex.color == VertexColor.WHITE:
                        vertex.color = VertexColor.GRAY
                        vertex.distance = u.distance + 1
                        vertex.pi = u
                        q.append(vertex)
                
                u.color = VertexColor.BLACK

    def printPath(self, s, v):

        if v == s:
            print(s.data.index)
        elif v.pi == None:
            print("No path found!")
        else:
            self.printPath(s, v.pi)
            print(v.data.index)

    def DFS(self):

        for vertex in self.graph:
            vertex.color = VertexColor.WHITE
            vertex.pi = None

        for vertex in self.graph:
            if vertex.color == VertexColor.WHITE:
                self.dfsVisit(vertex)

    def dfsVisit(self, vertex):
        self.time = self.time + 1
        vertex.time = self.time
        vertex.color = VertexColor.GRAY

        for v in vertex.neighbours:
            if v.color == VertexColor.WHITE:
                v.pi = vertex
                self.dfsVisit(v)

        vertex.color = VertexColor.BLACK
        self.time = self.time + 1
        vertex.finish = self.time

        self.topologicalSort.insert(0, vertex)

    def printTopologicalSort(self):

        for vertex in self.topologicalSort:
            print("index: ", vertex.data.index, ", discovered: ", vertex.time, ", finish:", vertex.finish)