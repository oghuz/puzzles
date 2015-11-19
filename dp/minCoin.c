#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

//recursive solution 
int minCoin(int N, int *coins, int len) {
  int i;
  for (i=0; i<len; i++)
    if (coins[i] == N)
      return 1;

  for (i=len; i>0; i--)
    if (coins[i-1] <N)
      break;

  if (i<=0)
    return -1; 

  int change = minCoin(N-coins[i], coins,i);
  return change >0 ? change + 1 : -1; 
}

int main(int argc, char** argv) {
	int coins[3] = {1,7,9};
  int len = 3; 
	int N = argc >1 ? atoi(argv[1]): 21;
  
	printf("challenge accepted !\n");
  printf("Minimum number coins to change %d is: %d\n", N, minCoin(N,coins,len));
	return 0;
}

