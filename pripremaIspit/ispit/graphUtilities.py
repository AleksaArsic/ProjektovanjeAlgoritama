import math

class Data:
    def __init__(self, data = None):
        self.d = data

class Vertex:
    def __init__(self, data = None):
        self.d = data
        self.edges = []

        # Dijkstra and Bellman-Ford
        self.distance = math.inf
        self.pi = None

    def addEdge(self, e = None):

        if isinstance(e, Edge):

            exists = False

            ed = None

            for edge in self.edges:
                if edge.d.d.d == e.d.d.d:
                    exists = True
                    ed = edge
                    break


            if not exists:
                self.edges.append(e)

                self.edges.sort(key = lambda x : x.w)

            else:
                print("Edge already exists!")

        else:
            print("Parameter must be Vertex instance!")

class Edge:
    def __init__(self, source = None, destination = None, weight = 0):
        self.s = source
        self.d = destination
        self.w = weight

class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, vertex = None):

        if isinstance(vertex, Vertex):
            self.vertices.append(vertex)
        else:
            print("Parameter must be Vertex instance!")

    def addEdge(self, edge = None):

        if isinstance(edge, Edge):

            v = None

            for vertex in self.vertices:
                if vertex.d.d == edge.s.d.d:
                    v = vertex
                    break

            if vertex != None:
                vertex.addEdge(edge)
            else:
                print("Vertex not in graph!")
                
        else:
            print("Parameter must be Edge instance!")

    def printGraph(self):

        for v in self.vertices:
            
            print("Vertex: ", v.d.d, "with Dijkstra/Bellman-Ford distance: ", v.distance)

            for e in v.edges:
                print("\tNeighbour:", e.d.d.d, " with weight to:", e.w)