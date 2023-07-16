CC = cc
CFLAGS = -std=c99 -Wall -fopenmp
LDFLAGS = -lm

jacobi: jacobi.c
	$(CC) $(CFLAGS) -o jacobi jacobi.c $(LDFLAGS)

jacobi_parallel: jacobi.c
	$(CC) $(CFLAGS) -o jacobi_parallel jacobi.c $(LDFLAGS) -D _OPENMP

.PHONY: clean

clean:
	rm -f jacobi jacobi_parallel
