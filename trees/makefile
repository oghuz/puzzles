
CC=gcc -std=gnu99 -Wall -O3
LIBS=-lm -lrt

default: connectBSTbyLevel

connectBSTbyLevel: binary.tree.connect.level.c
	$(CC) -o $@ $<

clean:
	rm -f connectBSTbyLevel
