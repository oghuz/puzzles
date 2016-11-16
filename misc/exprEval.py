#!/usr/bin/env python

import sys

def doArthimetic(a,b,op):
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

def extractMulDiv(expression):
    

def exprEval(expression):
    stack = []
    op = '' 
    for char in expression:
        if char == ' ':
            continue
        elif char == '*' or char == '/' or char =='+' or char == '-':
            op = char
        else:
            if len(stack) >0:
                a = stack[-1]
                b = int(char)
                stack [-1] = doArthimetic(a,b,op)
            else:
                stack.append(int(char)) 
    return stack[-1] if len(stack) >0 else None
    



def main():
    if len(sys.argv) <3:
        print msg()
        sys.exit(0)

    text = sys.argv[1].strip()
    pattern = sys.argv[2].strip()

    simple_test_case()
    
    # if match(text, pattern):
    if match_nospace(text, pattern):
        print "Yes"
    else:
        print "No"
print exprEval(' ')
print exprEval('1')
print exprEval('1 + 2 * 3')
print exprEval('1 + 2 * 3 + 1')

if __name__ == '__main__':
    main()

