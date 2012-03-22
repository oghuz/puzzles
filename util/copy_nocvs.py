#!/usr/bin/python

import os
import shutil
import sys

def main():
    if len(sys.argv) !=3 :
	print "Missing argument."
	print "Usage: copynocvs [source_dir] [target] "
	sys.exit("program terminated without eecution.")

    SOURCE_DIR = sys.argv[1]
    TARGET_DIR = sys.argv[2]

    IGNORE_PATTERNS = ('*.pyc','CVS','^.git','tmp','.svn')
    if os.path.exists(TARGET_DIR):
	shutil.rmtree(TARGET_DIR)
    shutil.copytree(SOURCE_DIR, TARGET_DIR, ignore=shutil.ignore_patterns(IGNORE_PATTERNS))

if __name__ == '__main__':
    main()

