# 
#  The g++ options are for linking in hdf5 libraries.
#


all: gpu-cover

UNAME 		= $(shell uname)
DFLAGS      = -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_BSD_SOURCE
OPTFLAGS    = -O3 -g 
INCFLAGS    = -I. -I/usr/local/include
CFLAGS      = $(OPTFLAGS) $(DFLAGS) $(INCFLAGS) 
LDFLAGS     = $(OPTFLAGS)
LIBS        = -L/usr/local/lib /usr/local/lib/libhdf5_hl.a /usr/local/lib/libhdf5.a -lz -lm 
CUDADFLAGS  = -ldl -rdynamic $(OPTFLAGS)
CUDACFLAGS  = -arch compute_11$ 

ifeq ($(UNAME), Darwin)
CUDALIBS    = -L/usr/local/cuda/lib -lcudart
CUDALINKOPT = -Xlinker -pie
CC = g++ -arch x86_64
else 
CUDALIBS    = -L/usr/local/cuda/lib64 -lcudart
CC = g++
endif
NVCC = nvcc -m64

HFILES		= gpu_cover_tree.h


gpu_cover_tree.o: gpu_cover_tree.cu $(HFILES)
	$(NVCC) $(CUDACFLAGS) -c $*.cu

main.o: main.cpp $(HFILES)
	$(CC) $(CFLAGS) -c $*.cpp


gpu-cover: gpu_cover_tree.o main.o
	$(CC) $(LDFLAGS) -o gpu-cover main.o gpu_cover_tree.o $(LIBS) $(CUDALIBS)
#	$(NVCC) $(CUDALINKOPT) -o gpu-cover gpu_cover_tree.o $(CUDALIBS)

clean:
	rm -f *.o gpu-cover
	

