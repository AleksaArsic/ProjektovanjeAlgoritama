import math

class Data:

    def __init__(self, d):
        self.data = d

class Vertex:

    def __init__(self, data = None):
        self.d = data
        self.edges = []

        # Dijkstra variables
        self.distance = math.inf
        self.pi = None

    def addEdge(self, edge = None):

        if isinstance(edge, Edge):

            exists = False
            ed = None

            for e in self.edges:
                if e.d.d.data == edge.d.d.data:
                    exists = True
                    ed = e
                    break

            if not exists:
                self.edges.append(edge)
                self.edges.sort(key = lambda x: x.w)

                print("Edge from: ", edge.s.d.data, " to: ", edge.d.d.data, " with weight:", edge.w, " added!")
            else:

                ed.w = edge.w
                self.edges.sort(key = lambda x: x.w)

                print("Edge from vertex: ", edge.s.d.data, " to vertex: ", edge.d.d.data, " already exists!")
                print("Weight updated: ", edge.w)
        else:
            print("Error! You are passing wrong object as an argument.")

class Edge:

    def __init__(self, source = None, destination = None, weight = None):
        self.s = source
        self.d = destination
        self.w = weight

class Graph:

    def __init__(self):
        self.vertices = []

    def addVertex(self, vertex = None):

        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices.append(vertex)
            self.vertices.sort(key = lambda x: x.d.data)

        else:
            print("Error! Vertex may be a part of graph or you are passing wrong object as an argument.")

    def addEdge(self, edge = None):

        if isinstance(edge, Edge):
            
            v = None

            for vertex in self.vertices:
                if vertex.d.data == edge.s.d.data:
                    v = vertex
                    break

            if v != None:
                v.addEdge(edge)
            else:
                print("There is no such vertex: ", edge.s)
        else:
            print("Error! You are passing wrong object as an argument.")

    def printGraph(self):

        print("\n***********************   GRAPH   ***********************")

        for v in self.vertices:
            print("Vertex: ", v.d.data, " and distance: ", v.distance)
            for e in v.edges:
                print("\tEdge to: ", e.d.d.data, " with weight: ", e.w, " and distance: ", e.d.distance)

        print("\n*********************************************************")

# if vertex points to itself that adds two to the degree
def getInDegrees(graph = None):
    
    degrees = []
    degree = 0

    if isinstance(graph, Graph):

        for v in graph.vertices:

            degree = 0

            for l in graph.vertices:
                
                for e in l.edges:
                    if e.d.d.data == v.d.data:
                        degree += 1

            degrees.append((v.d.data, degree))

    else:
        print("Error! You need to pass Graph object to function.")

    return degrees

def getOutDegrees(graph = None):
    
    degrees = []
    degree = 0

    if isinstance(graph, Graph):

        for v in graph.vertices:
            degree = len(v.edges)

            for e in v.edges:
                if e.d.d.data == v.d.data:
                    degree += 1

            degrees.append((v.d.data, degree))
    else:
        print("Error! You need to pass Graph object to function.")

    return degrees

def updateEdge(graph = None, nodeA = None, nodeB = None,  weight = None):

    if isinstance(graph, Graph) and isinstance(nodeA, Vertex) and isinstance(nodeB, Vertex):
        
        e = Edge(nodeA, nodeB, weight)

        graph.addEdge(e)
    else:
        print("Error! Check passing arguments.")