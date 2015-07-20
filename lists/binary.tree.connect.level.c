#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // INT_MAX

typedef struct node
{
  int data;
  struct node *left, *right, *cousin;
} node;

node *createNode(int data){
	node * n = (node*)malloc(sizeof(node));
	n->left = NULL; // points to last node 
	n->right= NULL; // points to next node 
	n->cousin = NULL; // points to the first node 
	n->data = data; // holds info 
	return n;
}

node *createQueue(){
	return createNode(-1);
}

void enqueue(node* q, node* item){
	node* n = createNode(0);
	n->cousin = item; 
	
	node * last = q->left; 
	if (NULL == last){
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


// a queue based approach that fails for large structure
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

node* simpleTree(int N){
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

// get newphew or niece 
node *getNN(node *p) 
{
    node *n = p; 
    while ((n = n->cousin) != NULL)
    {
        if (n->left != NULL)
            return n->left;
        if (n->right != NULL)
            return n->right;
    }
    return NULL;
}


void connectByLevel(node* p)
{
    node *temp;
 
    if (!p)
      return;
 
    // Set cousin for root
    p->cousin = NULL;
 
    // set cousin of all levels one by one
    while (p != NULL)
    {
        node *q = p;
 
        /* Connect all childrem nodes of p and children nodes of all other nodes
          at same level as p */
        while (q != NULL)
        {
            // Set the cousin pointer for p's left child
            if (q->left)
            {
                // If q has right child, then right child is cousin of
                // p and we also need to set cousin of right child
                if (q->right)
                    q->left->cousin = q->right;
                else
                    q->left->cousin = getNN(q);
            }
 
            if (q->right)
                q->right->cousin = getNN(q);
 
            // Set cousin for other nodes in pre order fashion
            q = q->cousin;
        }
 
        // start from the first node of next level
        if (p->left)
           p = p->left;
        else if (p->right)
           p = p->right;
        else
           p = getNN(p);
    }
}

int main(int argc, char** argv) {
	const int N = argc >1 ? atoi(argv[1]): 7;

	printf("challenge accepted !\n");

	node *t =  simpleTree(N);;
	inspect(t);

	printf("--------------------------------\n");
	connectByLevel(t);
	inspect(t);
	inspectByLevel(t);



	return 0;
}
