
CC=gcc -std=gnu99 -Wall -O3
LIBS=-lm -lrt

default: christmasTree reverseList

christmasTree: binary.tree.connect.level.c
	$(CC) -o $@ $<

reverseList: reversing.a.list.c
	$(CC) -o $@ $<

clean:
	rm -f reverseList christmasTree
