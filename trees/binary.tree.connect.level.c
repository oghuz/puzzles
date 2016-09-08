#include "bst.h"

node *createQueue(){
  return createNode(-1);
}

void enqueue(node* q, node* item){
  node* n = createNode(0);
  n->cousin = item; 

  node * last = q->left; 
  if (last == NULL){
    q->right = n ;
    q->cousin = n;
  }
  else 
    last->right =n;

  q->left = n;
}

node* dequeue(node* q){ // deturns data pointer 
  if (q == NULL || q->right ==NULL)
    return NULL;

  node * n = q->right;
  q->right = n->right;
  if (q->right == NULL)
    q->left = NULL;
  q->cousin = n->cousin;
  free(n);
  return q->cousin;
}

void destroyQueue(node* q){
  node * n = NULL;
  while ((n = dequeue(q)) != NULL)
    free(n);
  free(q);
}

/* // a queue based approach that fails for large structure
void connect(node *root){
  node* q = createQueue();
  root->cousin = NULL;
  enqueue(q, root->left);
  enqueue(q, root->right);

  node * n = NULL; 
  while ((n = q->left) != NULL)
  {
    node* a = dequeue(q);
    enqueue(q,a->left);
    enqueue(q,a->right);
    do {
      node* b = dequeue(q);
      a->cousin = b;

      enqueue(q,b->left);
      enqueue(q,b->right);
      a = b ; 
    } while(a!= n);
  }
}
*/

void inspectByLevel(node* root) {
  if (root == NULL) return;
  printf("%d\n", root->data);
  node * n = NULL;
  while ((n = root->left) != NULL) // depth 
  {
    do {
      printf("%d,", n->data);
    }
    while((n = n->cousin )!= NULL);
    root = root->left;
    printf("\n");

  }
}

void inspect(node* root) {
  if (root == NULL) return;

  node* q = createQueue();
  enqueue(q, root);
  node * n = NULL;
  while ((n = dequeue(q)) != NULL)
  {
    enqueue(q,n->left);
    enqueue(q,n->right);
    printf("%d,", n->data);
  }
  printf("\n");
}

node* createTree(int N){
  int i =0;
  node * root = createNode(i++);

  /*root->left = createNode(i++);
    root->right = createNode(i++);
    root->left->left = createNode(i++);
    root->left->right = createNode(i++);
    root->right->left = createNode(i++);
    root->right->right = createNode(i++);
    */

  node * q = createQueue();
  enqueue(q,root);
  node *n = NULL;
  while (i<N)
  {
    n = dequeue(q);
    n->left = createNode(i++);
    enqueue(q, n->left);
    n->right = createNode(i++);
    enqueue(q, n->right);
  }
  return root;
}

// get newphew/niece 
node* getNN(node *n){
  while ((n= n->cousin) != NULL)
  {
    if (n->left != NULL){
      return n->left;
    }
    if (n->right != NULL){
      return n->right;
    }
  }
  return NULL;
}

void connectByLevel(node* t)
{
  if (NULL == t)
    return;
  t->cousin = NULL; // special case for root

  while (t != NULL) {
    node *n = t;
    while (n != NULL)
    {
      if (n->left != NULL)
        n->left->cousin = n->right != NULL ? n->right : getNN(n);

      if (n->right != NULL)
        n->right->cousin = getNN(n);

      n= n->cousin;
    }
    // t = (t->left !=NULL) ? t->left : (t->right != NULL ? t= t->right : getNN(t));
    if (t->left != NULL){
      t = t->left;
    }
    else if (t->right != NULL){
      t = t->right;
    }
    else {
      t = getNN(t);
    }
  }
}

int main(int argc, char** argv) {
  const int N = argc >1 ? atoi(argv[1]): 7;
  printf("challenge accepted !\n");
  node *t =  createTree(N);;
  inspect(t);
  printf("--------------------------------\n");
  //connect(t);
  connectByLevel(t);
  inspect(t);
  inspectByLevel(t);
  return 0;
}
