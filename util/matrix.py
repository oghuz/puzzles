#! /usr/bin/python

import random
from time import *

def zero(m,n):
    # Create zero matrix
    new_matrix = [[0 for row in range(n)] for col in range(m)]
    return new_matrix

def rand(m,n):
    # Create random matrix
    new_matrix = [[random.random() for row in range(n)] for col in range(m)]
    return new_matrix

def show(matrix):
    # Print out matrix
    for col in matrix:
        print col 

def add(matrix1,matrix2):
    # Matrix addition
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        # Check matrix dimensions
        print 'Matrices must be m*n and m*n to add!'
    else:
        # Multiply if correct dimensions
        new_matrix = zero(len(matrix1),len(matrix1[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                    new_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
        return new_matrix
    
def mult(matrix1,matrix2):
    # Matrix multiplication
    if len(matrix1[0]) != len(matrix2):
        # Check matrix dimensions
        print 'Matrices must be m*n and n*p to multiply!'
    else:
        # Multiply if correct dimensions
        new_matrix = zero(len(matrix1),len(matrix2[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        return new_matrix

def time_mult(matrix1,matrix2):
    # Clock the time matrix multiplication takes
    start = clock()
    new_matrix = mult(matrix1,matrix2)
    end = clock()
    print 'Multiplication took ',end-start,' seconds'

# def profile_mult(matrix1,matrix2):
    # A more detailed timing with process information
    # Arguments must be strings for this function
    # eg. profile_mult('a','b')
#    cProfile.run('matrix.mult(matrix1,matrix2)')


def main ():
    m1 = rand(3,3)
    show (m1)
    print ""
    m2 = rand(3,3)
    show (m2)
    print ""
    show(mult(m1,m2))
    print ""
    show(add(m1,m2))
    # time_mult(m1,m2)


if __name__ == '__main__':
    main()

