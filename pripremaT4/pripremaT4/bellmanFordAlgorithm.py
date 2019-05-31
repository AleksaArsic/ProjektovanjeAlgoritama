import math

from graphUtilities import *
from pripremaT4 import *

def bellmanFordAlgorithm(graph = None, source = None):
    
    if isinstance(graph, Graph) and isinstance(source, Vertex):
        
        initializeSingleSource(graph, source)

        for i in range(len(graph.vertices) - 1):
            for u in graph.vertices:
                for v in u.edges:
                    relax(u, v.d, v.w)

        for i in range(len(graph.vertices) - 1):
            for u in graph.vertices:
                for v in u.edges:
                    if v.d.distance > (u.distance + v.w):
                        return False

        return True
    else:
        print("Error! Check passing arguments.")
        return False

def initializeSingleSource(graph = None, source = None):

    for v in graph.vertices:
        v.distance = math.inf
        v.pi = None

    source.distance = 0

def relax(u = None, v = None, w = None):

    if isinstance(u, Vertex) and isinstance(v, Vertex):
        if v.distance > (u.distance + w):
            v.distance = (u.distance + w)
            v.pi = u
    else:
        print("Error! Check passing arguments.")
