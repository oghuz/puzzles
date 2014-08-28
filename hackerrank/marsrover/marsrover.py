#!/usr/bin/env python

import sys
from collections import defaultdict

def build_interval_tree(intervals):
    """
    I choose not to use this approach for simplicity.
    """
    return None

def overlaps(a,b):
    """
    returns a boolean value that is true if the two intervals a and b overlap
    """
    return b[0] <= a[1] and a[0] <= b[1]

def popmin(pqueue):
    """
    pops the minumim value item from the queue
    in this problem it would be the minimum distance
    """
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest

def dijkstra(graph, source, target):
    """
    dijkstra's shortest path algorithm for finding the shortest path between
    source and target 
    """
    pqueue = {} 
    dist = {}
    pred = {}

    for v in graph:
        dist[v] = 1000
        pred[v] = -1
    dist[source] = 0
    for v in graph:
        pqueue[v] = dist[v]
 
    while pqueue:
        u = popmin(pqueue)
        if u == target:
            break
        for v in graph[u].keys():
            w = graph[u][v]
            newdist = dist[u] + w
            if (newdist < dist[v]):
                pqueue[v] = newdist
                dist[v] = newdist
                pred[v] = u
 
    return dist, pred

def mars_rover(graph, source, target):
    """
    Reduced the mars_rover problem to a graph problem in which 
    shortest path between source and target represents the sequence of image
    snapshos that need to be downloaded.
    vertex represents the starting and end point of image segments
    edge represtens the transmission cost.
    """
    dist, pred = dijkstra(graph, source, target)
    if target in dist:
        print("%.3f" %dist[target])

if __name__=='__main__':
    N = int (sys.stdin.readline().strip())
    L = int (sys.stdin.readline().strip())
    B = int (sys.stdin.readline().strip())
    C = int (sys.stdin.readline().strip())
    intervals = []
    i = 0
    for line in sys.stdin:
        if i < C:
            chunk = [int(x) for x in line.strip().split(',')]
            intervals.append(chunk) # here I did not concern duplicate intervals

    # sort intervals by their starting point
    intervals = sorted(intervals, key=lambda intervals:intervals[0]) 
    intervals.insert(0,[0,0])
    intervals.append([N,N])
    
    #print (N,L,B,C)
    #print intervals
    
    graph = defaultdict(dict)
    origin = [0,0]
    nv = len(intervals) 

    for i in xrange(nv):
        if i < nv - 1:
            for j in xrange(i+1,nv):
                if overlaps(intervals[i],intervals[j]):
                    w = 2 * L + float(intervals[j][1] - intervals[j][0])/float(B)
                    graph[i][j] = w
    mars_rover(graph,0 , C)

