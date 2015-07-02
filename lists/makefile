
CC=gcc -std=gnu99 -Wall -O3
LIBS=-lm -lrt

default: program

program: reversing.a.list.c
	$(CC) -o $@ $<

clean:
	rm -f program 
