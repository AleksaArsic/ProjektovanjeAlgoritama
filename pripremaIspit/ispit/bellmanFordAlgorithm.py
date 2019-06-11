import math
from graphUtilities import *

def initSingleSource(G, s):
    for v in G.vertices:
        v.distance = math.inf
        v.pi = None

    s.distance = 0

def relax(u, v, w):
    if v.distance > (u.distance + w):
        v.distance = u.distance + w
        v.pi = u

def bellmanFordAlgortihm(G, s):

    initSingleSource(G, s)

    for i in range(len(G.vertices) - 1):
        for v in G.vertices:
            for e in v.edges:
                relax(v, e.d, e.w)

    for v in G.vertices:
        for e in v.edges:
            if v.distance > (e.d.distance + e.w):
                return False

    return True
