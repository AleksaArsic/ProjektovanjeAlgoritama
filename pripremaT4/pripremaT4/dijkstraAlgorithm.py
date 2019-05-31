import math

from graphUtilities import *

def dijkstraAlgorithm(graph = None, source = None):

    if isinstance(graph, Graph) and isinstance(source, Vertex):
        
        initializeSingleSource(graph, source)

        s = []
        queue = graph.vertices.copy()

        while len(queue):

            queue.sort(key = lambda x: x.distance)

            u = queue.pop(0)
            s.append(u)

            for e in u.edges:
                relax(u, e.d, e.w)

    else:
        print("Error! Check passing arguments.")

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

def shortestPath(graph = None, nodeA = None, nodeB = None):

    if isinstance(graph, Graph) and isinstance(nodeA, Vertex) and isinstance(nodeB, Vertex):

        dijkstraAlgorithm(graph, nodeA)

        shortest = []
        node = nodeB
        distance = nodeB.distance

        while node.pi != None:
            shortest.append(node.pi)
            node = node.pi

    else:
        print("Error! Check passing arguments.")
    
    shortest.reverse()

    return (shortest, distance)