#! /usr/bin/env python 

import sys
import math


def lookup_lcs(i,j,cache,t):
    # print "calling [%d,%d]" % (i,j)
    if i <0 or j <0:
        return 0

    (x,y) = t
    if cache[i][j] <0:
        if x[i] == y[j]:
            cache[i][j] = lookup_lcs(i-1,j-1,cache,t) + 1
        else:
            cache[i][j] = max(lookup_lcs(i-1,j,cache,t),lookup_lcs(i,j-1,cache,t))
    return cache[i][j]


def memoized_lcs(x,y):
    n = len(x)
    m = len(y)
    cache = [[-1 for i in xrange(m) ] for j in xrange(n)]
    # print lookup_lcs(len(x)-1,len(y)-1,cache,(x,y))
    return cache

def lcs(x,y):
    n = len(x)
    m = len(y)
    c = [[0 for i in xrange(m) ] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(m):
            if x[i] == y[j]:
                c[i][j] = (c[i-1][j-1] if i>0 and j>0 else 0) + 1 
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j] if i>0 else 0
            else:
                c[i][j] = c[i][j-1] if j >0 else 0
    return c

def getSolution(c,x,y):
    #print "x=[%s], y=[%s]" % (x,y)
    n = len(x)
    m = len(y)
    #print "n=[%d], m=[%d]" % (n,m)
    if n == 0 or m == 0:
        return ""
    if x[-1] == y[-1]:
        return getSolution(c,x[:-1],y[:-1]) + x[-1]
    elif c[n-1][m-1] == (c[n-2][m-1] if n>1 else -1):
        return getSolution(c,x[:-1],y)
    else:
        return getSolution(c,x,y[:-1])


def main ():
    if len(sys.argv) < 3:
        print "Usage: " + sys.argv[0] +" X Y"
        exit(1) 

    x = sys.argv[1].strip()
    y= sys.argv[2].strip()
    cost_matrix  = lcs(x,y)
    for i in cost_matrix:
        print i
    cost_matrix  = memoized_lcs(x,y)
    for i in cost_matrix:
        print i
    #print getSolution(cost_matrix,x,y)


if __name__ == '__main__':
    main()

