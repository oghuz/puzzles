#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

typedef struct node
{
  int data;
  struct node *left, *right;
} node;

node *createNode(int data){
  node * n = (node*)malloc(sizeof(node));
  n->left = NULL; // points to last node 
  n->right= NULL; // points to next node 
  n->data = data; // holds info 
  return n;
}

node* createTree(int N){
  int i =0;
  node * root = createNode(i++);

  root->left = createNode(i++);
  root->right = createNode(i++);
  root->left->left = createNode(i++);
  root->left->right = createNode(i++);
  root->right->left = createNode(i++);
  root->right->right = createNode(i++);

  return root;
}

int main(int argc, char** argv) {
  const int N = argc >1 ? atoi(argv[1]): 7;
  printf("challenge accepted !\n");
  node *t =  createTree(N);;
  printf("--------------------------------\n");
  return 0;
}
