#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

#define max(a,b) ({ __typeof__ (a) _a = (a); __typeof__ (b) _b = (b); _a > _b ? _a : _b; })
#define min(a,b) ({ __typeof__ (a) _a = (a); __typeof__ (b) _b = (b); _a > _b ? _b : _a; })


//recursive solution 
int minCoin(int N, int *coins, int len) {
	int i;
	for (i=0; i<len; i++)
		if (coins[i] == N)
			return 1;

	for (i=0; i <len; i++)
		if (coins[i] >N)
			break;

	if (i==0)
		return -1;

	int change = minCoin(N-coins[i-1], coins,i);
	if (change > 0)
		change +=1;
	int change2 = minCoin(N,coins,len-1); 

	return min(change,change2) > 0 ? min(change,change2): max(change,change2); 
}

int main(int argc, char** argv) {
	int coins[3] = {1,7,9};
	int len = 3; 
	int N = argc >1 ? atoi(argv[1]): 21;

	printf("challenge accepted !\n");
	printf("Minimum number coins to change %d is: %d\n", N, minCoin(N,coins,len));
	return 0;
}

