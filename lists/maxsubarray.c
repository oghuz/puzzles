#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

void max_subarray(int * arr, int *idx, int size) {
	int currentMaxSum = 0;
	int currentStartIndex = 0;
	int maxEndIndex = 0;
	int maxStartIndex = 0;
	int maxSum=0;
	for (int i =0; i < size; i++)
	{ 
		currentMaxSum = currentMaxSum + arr[i];
		if (currentMaxSum > maxSum){
			maxSum = currentMaxSum;
			maxStartIndex = currentStartIndex; 
			maxEndIndex = i;

		}
		if (currentMaxSum < 0){
			currentMaxSum = 0;
			currentStartIndex = i + 1;
		}
	}
	idx[2] =  maxSum; 
	idx[0] = maxStartIndex;
	idx[1] = maxEndIndex;
	return;
}
int main(int argc, char** argv) {
	//const int N = argc >1 ? atoi(argv[1]): 9;
	const int N = 9;

	int arr[9] = {-2,1,-2,4,-1,2,1,-5,4};
	printf("challenge accepted !\n");

	int bound[3] = {-1,-1,0}; 


	max_subarray(arr, bound, N);
	for (int i=bound[0]; i< bound[1]; i++)
		printf("%d, ", arr[i]);
	printf("%d\n", arr[bound[1]]);

	printf("sum is: %d\n", bound[2]);

	return 0;
}

