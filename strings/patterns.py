#!/usr/bin/env python

import sys

def exhaustive(text, pattern, mapping, table):
    if len(text) ==0 and len(pattern)==0:
        return True
    else:
        if len(text) ==0 or len(pattern)==0:
            return False

    pairs = [(text[0:i+1], text[i+1:]) for i in xrange(len(text))]
    
    c = pattern[0]
    for word,remain in pairs:
        if word in mapping and mapping[word] == c and exhaustive(remain,pattern[1:],mapping,table):
            return True
        elif table[c]:
            mapping[word] = c
            table[c] = False
            if exhaustive(remain,pattern[1:],mapping,table):
                return True
            del mapping[word]
            table[c] = True
        else:
            continue
    return False

def match_nospace(text, pattern, print_flag=False):
    table = {char : True for char in pattern}
    mapping = {}
    res = exhaustive(text,pattern,mapping,table)
    if print_flag:
        print mapping
    return res


def match(text, pattern):
    table = {char : True for char in pattern} # symbol table for unused symbols
    mapping = {}
    words = text.split()
    if len(words) != len(pattern):
        return False

    for i, word in enumerate(words):
        c = pattern[i]
        symbol = mapping.get(word)
        if symbol: # mapping for this word exists
            if c != symbol:
                return False
        else:
            if table[c]: # if the corresponding symbol was not mapped 
                table[c] = False
                mapping[word] = c
            else:
                return False
    return True


def simple_test_case():
    cases = [("redgreenblue", "abc", True), ("redgreengreen", "xyz", True), ("redgreenblue", "xyy", False),("dogcatcat", "xyy", True)]
    for text,pattern,res in cases:
        if match_nospace(text,pattern) != res:
            print "Test [%s ---> %s] fails." % (text,pattern)
            return False
    return True

def msg():
    return '''patterns: matches the given string against a pattern
    Usage: pattern arg1 arg2
    Example: patterns "red green blue" "abc" '''

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

if __name__ == '__main__':
    main()

