#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

typedef struct node
{
  int data;
  struct node *next;
} 
node;

node *init(int N);
int testme(node * list);
int testlabel(node* list);
void inspect(node * list);

	
node *label(node *list);
node *reverse(node *list);
node *reverseN(int N, node *list);

int main(int argc, char** argv) {
  const int N = argc >1 ? atoi(argv[1]): 10;

  int i = N;
  printf("challenge accepted !\n");

  node *list =  init(i);
  //inspect(list);

  label(list);
  //inspect(list);
  printf("test label %s\n", testme(list) ? "pass.": "fail.");

  list = reverse(list);
  list = reverse(list);
  int t = testme(list);
  printf("test reverse %s\n", t ? "pass.": "fail.");

  list = reverseN(2, list);
  //inspect(list);
  list = reverseN(2, list);
  //inspect(list);
  t = testme(list);
  //inspect(list);
  printf("test reverseN %s\n", t ? "pass.": "fail.");
  return 0;
}

int testlabel(node* list) {
  int flag = 1; 
  while (NULL != list)
  {
	  if (list->data != 0){
		  flag =0;
		printf("problem %d !\n", list->data);
		  break;
	  }
	  list = list->next;
  }
  return flag;
}
int testme(node* list) {
	int flag = 1;
	int i = 1 ; 
	while (NULL != list)
	{
		if (list->data != i ){
			flag = 0;
			printf("problem %d -- %d!\n", i, list->data);
			break;
		}
		list = list->next;
		i++;
	}
	return flag; 
}

void inspect(node* list) {
	while (NULL != list)
	{
		printf("data -> %d\n", list->data);
		list = list->next;
	}
	printf("-------------------------------------!\n");
}

node * init(int N)
{
	N = N-1; 
	int i =0;
	node * list = (node*)malloc(sizeof(node));
	list->data = i;
	list->next = NULL;
	node * n =list;

	while (i < N )
	{
		i++;
		n->next= (node*)malloc(sizeof(node));
		n->next->data = 0;
		n->next->next = NULL;
		n = n->next;
	}
	return list;
}

node *label(node *list){
	node * current_node = list; 
	int seq =0;

	// edge case 
	if (NULL == current_node)
		return NULL;

	// if the list contains more than INT_MAX number of elements, I decide not to label them.
	while (current_node != NULL && seq < INT_MAX)
	{
		current_node->data = ++seq; 
		current_node = current_node->next; 
	}

	return list;
}

// I use a recursive approach(head came to my mind), while it may not so nice to the stack. 
/*node *reverse(node *list){
  node* head;
  node* tail;

  if (NULL == list)
  return NULL;   

  tail = list->next;  
  head = reverse(tail);
  if (NULL == head)
  return list; 

  list->next = tail->next;
  tail->next = list;

  return head;
  }*/
node* reverse(node* list)
{
	node* nodes[3] = {NULL, list,NULL}; // previous, current and next nodes in the list 
	while (NULL != nodes[1])
	{
		nodes[2] = nodes[1]->next;  
		nodes[1]->next = nodes[0];   
		nodes[0] = nodes[1];
		nodes[1] = nodes[2];
	}
	return nodes[0];
}

// I don't like this verbose solution, but it is stack friendly I guess.
node *reverseN(int N, node *list){
	node * root = NULL;
	if (N <= 0) {
		printf("I can not reverse the list with %d step size.!\n", N);
		return list;
	}
	else if (1 == N )
		return reverse(list);
	else {
		node* head =list;
		node* tail = head;
		int counter =1;

		if (NULL == head )
			return NULL;

		while (counter++ < N && NULL != (head = head->next));
		counter =1;
		if (NULL != head ){
			list = head->next;
			head->next = NULL;
		}
		else 
			list = NULL;

		root = reverse(tail); // reverse the first part
		head = list;

		while (NULL != head ) {
			node* temp= head ;
			while (counter++ < N && NULL != (head = head->next));
			counter =1;
			
			if (NULL != head){
				list = head->next;
				head->next =NULL;
			}
			else 
				list = NULL; 
			tail->next = reverse(temp); // reverse the first part
			tail = temp;
			head = list ;
		}
		return root;
	}
}

