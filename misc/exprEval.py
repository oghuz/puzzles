#!/usr/bin/env python

import sys
import unittest

class State:
    EVAL = 0
    PROCESS = 1

def doArthmetic(a,b,op):
    val =None
    if op == '*':
        val = a *b
    elif op == '/':
        val = a/b
    elif op == '+':
        val = a +b
    elif op =='-':
        val = a-b
    else :
        val = None
    return val 

def exprEval(expression):
    val = None
    num_stack = []
    op_stack = []
    state = State.PROCESS
    
    for char in expression:
        if char == ' ':
            continue
        elif char== '*' or char =='/':
            op_stack.append(char)
            state = State.EVAL
        elif char== '+' or char =='-':
            op_stack.append(char)
            if len(op_stack) > 1:
                state = State.EVAL
        elif char >='0' and char <= '9':
            if state == State.EVAL:
                a = num_stack.pop()
                b = int(char)
                op = op_stack.pop()
                num_stack.append(doArthmetic(a,b,op))
                state = State.PROCESS
            else:
                num_stack.append(int(char)) 
        else:
            continue
    if len(op_stack)>0:
        a = num_stack.pop()
        b = num_stack.pop()
        op= op_stack.pop()
        val = doArthmetic(a,b,op)
    else:
        val = num_stack.pop() if len(num_stack) else None
    return val
    

class ExprEvalTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(exprEval(' '),None)
    
    def test_singleNumber(self):
        self.assertEqual(exprEval('1'),1)
    
    def test_simplePriority(self):
        self.assertEqual(exprEval('1 +2 * 3'),7)
    
    def test_sameOperator(self):
        self.assertEqual(exprEval('1*1/1*1/1'),1)
        self.assertEqual(exprEval('1+1-1+1-1'),1)
    
    def test_complex(self):
        self.assertEqual(exprEval('1*2 + 3*4 + 1'),15)
   
if __name__ == '__main__':
    unittest.main()

