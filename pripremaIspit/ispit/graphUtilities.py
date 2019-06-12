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

        # BFS and DFS
        self.color = "White"
        self.dist = math.inf
        self.p = None

        self.disc = 0
        self.finish = 0

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

        # DFS
        self.time = 0
        self.topologicalSort = []

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

    def BFS(self, s):
        for v in self.vertices:
            v.color = "White"
            v.dist = math.inf
            v.p = None

        s.color = "Gray"
        s.dist = 0
        s.p = None

        queue = []
        queue.append(s)

        while len(queue):
            u = queue.pop(0)

            for e in u.edges:
                k = e.d

                if k.color == "White":
                    k.color = "Gray"
                    k.dist = u.dist + 1
                    k.p = u

                    queue.append(k)

            u.color = "Black"

    def printBFSpath(self, s, v):
        if v == s:
            print(s.d.d)
        elif v.p == None:
            print ("No path from: ", s.d.d, " to:", v.d.d, " exists.")
        else:
            self.printBFSpath(s, v.p)
            print(v.d.d)

    def DFS(self):
        for u in self.vertices:
            u.color = "White"
            u.p = None
        
        self.time = 0

        for u in self.vertices:
            if u.color == "White":
                self.DFSvisit(u)

    def DFSvisit(self, u):
        self.time = self.time + 1
        u.disc = self.time
        u.color = "Gray"

        for e in u.edges:
            v = e.d

            if v.color == "White":
                v.p = u
                self.DFSvisit(v)

        u.color = "Black"
        self.time += 1
        u.finish = self.time

        self.topologicalSort.append(u)
        