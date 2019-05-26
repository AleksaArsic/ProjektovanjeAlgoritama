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
        self.distance = math.inf
        self.color = color
        self.pi = None

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
                print("\t[", neighbour.data.index, "]:", neighbour.color, ", dist:", neighbour.distance)

            i += 1

    def BFS(self, start):
        
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