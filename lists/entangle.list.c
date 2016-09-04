#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

typedef struct node
{
  int data;
  struct node *next;
} 
node;

// testing and debugging code
node *init(int N);
void inspect(node * list);
node *label(node *list);

//the meat 
node *reverse(node *list);
void entangle(node *list);

int main(int argc, char** argv) {
  int N = argc >1 ? atoi(argv[1]): 10;

  printf("challenge accepted !\n"); //Give me a number which indicates number of nodes on a list, otherwise I'll assume it's 10
  printf("-------------------------------------\n");

  node *list =  init(N);
  //inspect(list);
  label(list);

  printf("Here is the list I'll entangle! \n");
  inspect(list);
  
  printf("Entanglment result is:\n");
  entangle(list);

  printf("\nWhat do you think ? \n\n");
  return 0;
}

void entangle(node* head)
{

  int size = (head ==NULL ? 0 : 1 ); // size of list 
  node * temp = head; 
  while ((temp = temp->next )!= NULL)  // O(N)
    size++;
  if (size <2)
    return ; // edge cases 
  //printf("list length us %d !\n", size);
  
  temp = head;
  /* get the sublist -- second half of the original list O(N/2) */
  for (int i = 0; i<size/2; i++)
    temp = temp->next; 

  temp = reverse(temp); // reverse the sublist O(N/2) 
  //inspect(temp);
  node *n1 = head; // the first half of the list
  node *n2 = temp; // the second half
  for (int i = 0; i<size/2; i++) // O(n/2) 
  {
    head = n1->next; 
    temp = n2->next;
    n1->next = n2;
    n2->next = n1;

    printf("%d -- %d\n", n1->data, n2->data);

    n1= head;
    n2= temp;
  }
}

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

void inspect(node* list) {
  while (NULL != list)
  {
    printf("node[%d]-> %d\n", list->data,list->data);
    list = list->next;
  }
  printf("-------------------------------------\n");
}

node * init(int N)
{
  node * list = (node*)malloc(sizeof(node));
  list->data = 0;
  list->next = NULL;
  node * n =list;

  int i =0;
  while (i < N-1 )
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

