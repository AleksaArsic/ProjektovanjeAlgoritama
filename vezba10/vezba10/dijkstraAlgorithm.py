import math

from graphUtilities import *

def Dijkstra(graph = None, start = None):

    if isinstance(graph, Graph) and isinstance(start, Vertex):

        initializeSinlgeSource(graph, start)

        s = []
        queue = graph.vertices.copy()

        while len(queue):

            queue.sort(key = lambda x: x.distance)
            u = queue.pop(0)
            s.append(u)

            for edge in u.edges:
                    Relax(u, edge.destination, edge.weight)

    else:
        print("Error! Check graph and start vertex parameters!")

def Relax(u = None, v = None, weight = None):

    if v.distance > (u.distance + weight):
        v.distance = u.distance + weight
        v.pi = u

def initializeSinlgeSource(graph = None, start = None):
    
    for vertex in graph.vertices:
        vertex.distance = math.inf
        vertex.pi = None

    start.distance = 0

def extractMinimum(queue = None):

    min = math.inf
    pos = math.inf

    for i in range(len(queue)):
        for j in range(len(queue.edges)):
            if queue.edges[j].weight < min:
                pos = j
