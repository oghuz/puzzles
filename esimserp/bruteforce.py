#!/usr/bin/python

import time
import sys


def variation(word):
    results = []
    return results

def bruteForce(word, vocab):

    return None

def main():

    if len(sys.argv) <2:
        print "Missing argument"
        sys.exit(0)
    
    DICTIONARY_PATH = "/usr/dictionary/words"
    TAB="\t"
    SPACE=" "
    word = sys.argv[1].strip()

    start = time.time()
    vocab = set(open(DICTIONARY_PATH, "rt").read().split())
    results = len(vocab)
    print results
    end = time.time()

    print "Search took %g s" % (end - start)

if __name__ == '__main__':
    main()

