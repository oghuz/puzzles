#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

int median(int l, int r);
int binarySearch(int * A, const int key, int l, int r);
int rotatedSearch(int * A, const int key, int l, int r);
void inspect (int * A, int size);

int main(int argc, char** argv) {

  const int key = argc >1 ? atoi(argv[1]): 3;

  int A[8] = {5,6,7,8,9,1,2,4};
  //int A[8] = {1,2,4,5,6,7,8,9};
  printf("challenge accepted !\n");

  inspect(A,8);

  //int index = binarySearch(A,key,0,7);
  int index = rotatedSearch(A,key,0,7);

  if(index >=0)
    printf("Key [%d] is at position: %d\n", key, index);
  else 
    printf("Key [%d] is NOT found.\n",key);

  return 0;
}

int median(int l, int r){
  //return (l+r)/2;
  return (l-r)/2 + r;
}


int binarySearch(int * A, const int key, int l, int r) {
  if (l>r) return -1;
  printf("BS: [%d, %d]\n",l,r);

  int mid = median(l,r);

  if (A[mid] == key)
    return mid;
  else if (key < A[mid])
    return binarySearch(A,key,l,mid-1);
  else 
    return binarySearch(A,key,mid+1,r);
}

int rotatedSearch(int * A, const int key, int l, int r) {
  if (l>r) return -1;
  printf("RS: [%d, %d]\n",l,r);
  
  int mid = median(l,r);

  if (key == A[mid]){
    return mid;
  }
  else if (A[l] < A[mid] ) { // case 1 
    if (A[l] <= key && key <= A[mid])
      return binarySearch(A,key,l,mid-1);
    else 
      return rotatedSearch(A,key,mid+1,r);
  }
  else{  //case 2 
    if (A[r] >= key && key >= A[mid])
      return binarySearch(A,key,mid+1,r);
    else 
      return rotatedSearch(A,key,l, mid-1);
  }
}

void inspect (int * A, int size){
  printf("A = [");
  for (int i=0; i<size-1; i++)
    printf("%d, ", A[i]);

  printf("%d]\n", A[size-1]);
}

