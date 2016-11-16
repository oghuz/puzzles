#! /usr/bin/env python 

import sys
import math

def solve(dimensions):
    pass

def printSolution():
    pass

def test():
    if solve([5,20,1,10,100]) == 7000:
        print "Test passed"
    else:
        print "Test failed"


def main ():
    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] +" X "
        exit(1) 

    dimensions = [int(i) for i in sys.argv[1].strip().split(",")]
    print dimensions
    cost = solve(dimensions)
    print cost

if __name__ == '__main__':
    main()

