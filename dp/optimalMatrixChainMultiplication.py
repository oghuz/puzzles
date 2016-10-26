#! /usr/bin/env python 

import sys
import math

def solve(dimensions):
    dim = len(dimensions) - 1
    m = [[float('inf') for i in xrange(dim)] for j in xrange(dim)]
    for i in xrange(dim):
        m[i][i] = 0

    for l in xrange(1,dim):
        for i in xrange(dim-l):
            j =  i + l
            # print "----------- M[%d,%d]" % (i,j)
            for k in xrange(i,j):
                # print "[%d,%d,%d] = [%d * %d * %d ]" % (i,k,j, dimensions[i], dimensions[k+1], dimensions[j+1])
                q = m[i][k] + m[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][dim-1]

def printSolution():
    pass

def test():
    if solve([5,20,1,10,100]) == 7000:
        print "Test passed"
    else:
        print "Test failed"


def main ():
    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] +" d_1, d_2, d_3, d_4...... where matrix A is [d_1 by d_2] and B is [d_2 by d_3] ...."
        exit(1) 

    dimensions = [int(i) for i in sys.argv[1].strip().split(",")]
    print "Matrix = %s" % dimensions
    cost = solve(dimensions)
    print "--------------------------------------"
    #for i in xrange(len(dimensions) - 1):
    #    print cost[i]
    print "Cost = %d" % cost

if __name__ == '__main__':
    main()

