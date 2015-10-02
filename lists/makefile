
CC=gcc -std=gnu99 -Wall -O3
LIBS=-lm -lrt

default: reverseList maxSum christmasTree

reverseList: reversing.a.list.c
	$(CC) -o $@ $<

maxSum: maxsubarray.c
	$(CC) -o $@ $<

christmasTree: binary.tree.connect.level.c
	$(CC) -g -o $@ $<

clean:
	rm -f reverseList maxSum christmasTree
