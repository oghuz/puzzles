
CC=gcc -Wall
LIBS=-lm -lrt

default: image binarysearch

image: rectangles.in.image.c
	$(CC) -o $@ $<

binarysearch: search.c
	$(CC) -o $@ $<

clean:
	rm -f image binarysearch
