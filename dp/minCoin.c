#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

#define max(a,b) ({ __typeof__ (a) _a = (a); __typeof__ (b) _b = (b); _a > _b ? _a : _b; })
#define min(a,b) ({ __typeof__ (a) _a = (a); __typeof__ (b) _b = (b); _a > _b ? _b : _a; })

//check table 
void checkTable(int N, int **table, int* coins, int len) {
  for (int j=0; j<N+1;j++){
    for (int i=0; i<len;i++){
      printf("T[%d,%d]=%d  ", coins[i], j, table[i][j]==INT_MAX ? -1: table[i][j]);
    }
    printf("\n");
  }
  return;
}

//free memory 
void freeTable(int N, int **table, int len) {
  for (int i=0; i<len;i++)
    free(table[i]);
  free(table);
  return;
}

//Dynamic Programming Approach, ssuming coins are sorted. 
int getMinCount(int N, int **table, int len) {
  if (N == 0)
    return 0; 
  int minSoFar =INT_MAX; 
  for (int i=0; i<len;i++)
    if (minSoFar > table[i][N])
      minSoFar = table[i][N];
  return minSoFar;
}


int minCoin(int N, int *coins, int len) {
  int i,j;
  int** table = (int**)malloc(len * sizeof(int*));
  for (i=0; i<len;i++)
    table[i]= (int*)malloc((N+1)*sizeof(int));

  //table initlization 
  for (i=0; i<len;i++)
    for (j=1; j<N+1;j++)
      table[i][j] = INT_MAX; 

  for (i=0; i<len;i++){
    table[i][0] =0;
    table[i][coins[i]] = 1;
  }

  //table filling procedure
  for (j=1; j<N+1;j++)
    for (i=0; i<len;i++)
      if (coins[i] <= j)
        table[i][j] = getMinCount(j-coins[i],table,len) + 1;

  //checkTable(N,table,coins,len);

  i = getMinCount(N,table,len);
  
  freeTable(N,table,len);

  return i; 
}

//recursive solution 
/*
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

// solution that contains at least one count of coins[i-1] 
int change = minCoin(N-coins[i-1], coins,i); 
if (change > 0)
change +=1;

// solution that does not contain any coins[len-1] 
int change2 = minCoin(N,coins,len-1); 

return min(change,change2) > 0 ? min(change,change2): max(change,change2); 
}
*/
int main(int argc, char** argv) {
  int coins[3] = {1,5,7};
  int len = 3; 
  int N = argc >1 ? atoi(argv[1]): 15;

  printf("challenge accepted !\n");
  printf("Minimum number coins to change %d is: %d\n", N, minCoin(N,coins,len));
  return 0;
}

