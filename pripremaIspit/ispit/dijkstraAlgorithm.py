import math

from graphUtilities import *

def initSingleSource(G, s):

    for v in G.vertices:
        v.distance = math.inf
        v.pi = None

    s.distance = 0

def relax(u, v, w):
    if v.distance > (u.distance + w):
        v.distance = (u.distance + w)
        v.pi = u

def dijkstraAlgorithm(G, s):

    initSingleSource(G, s)

    s = []

    queue = G.vertices.copy()

    while len(queue):

        # sort by distance
        queue.sort(key = lambda x : x.distance)


        u = queue.pop(0)
        s.append(u)


        for e in u.edges:
            relax(u, e.d, e.w)
