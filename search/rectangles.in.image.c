#include <stdio.h>
#include <stdlib.h>
/**
 * This is an interview question in which we are asked 
 * to find the top left coordinate of a black rectangle 
 * and its width and height given a black-white image of 1s and 0s.
 */

int* findBlackRectangle(int ** image);
void genImage(int x, int y, int width, int height);
int checkArguments(int x, int y, int width, int height);
void printInfo(int* info);
void printImage();

const static int size =10; 
int* image[10] = {NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL};

int main(int argc, char** argv) {
    if (argc!=5){
        printf("Missing arguments.\n");
        return 1; 
    }

    int x = atoi(argv[1]);
    int y = atoi(argv[2]);
    int width = atoi(argv[3]);
    int height = atoi(argv[4]);

    if (checkArguments(x,y,width,height)){
        printf("Arguments are out of boundary. Please provide a valid range less than [%d].\n", size);
        return 1;
    }

    genImage(x,y,width,height);
    printImage();

    int * info = findBlackRectangle(image);
    printInfo(info);

    // free space 
    for (int i =0; i <size; i++)
        free(image[i]);
    
    free(info);

    return 0;
}

int checkArguments(int x, int y, int width, int height){
    if (x >=size || y >=size || width >size || height >size)
        return 1;
    return 0;
}

int* findBlackRectangle(int ** image) {
    int * info = (int*)malloc(4*sizeof(int));
    info[0]=-1;
    info[1]=-1;
    info[2]=-1;
    info[3]=-1;

    for (int i=0; i<size; i++){
        for (int j=0; j< size; j++){
            if (image[i][j] == 0){
                info[0] = j; 
                info[1] = i;
                while (j < size && image[i][j] !=1)
                    j++;
                info[2] = j - info[0];  // width 
                break; 
            }
        }
        if (info[0] >=0){ // found a rectangle
            // printInfo(info);
            while (i < size && image[i][info[0]] !=1)
                i++;
            info[3] = i - info[1];
            break;
        }
    }

    return info;
}

void genImage(int x, int y, int width, int height){
    for (int i =0; i <size; i++)
        image[i] = (int*)malloc(size*sizeof(int));

    for (int i =0; i <size; i++)
        for (int j = 0; j < size; j++)
            image[i][j]=1; 
    if (x < 0)
        return;
    for (int i =0; i <height; i++)
        for (int j = 0; j < width; j++)
            image[y+i][x+j] = 0;
}

void printImage(){
    printf("-----------------------------------------------\n");
    for (int i=0; i < size; i++)
        printf("%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n",image[i][0], image[i][1], image[i][2], image[i][3], image[i][4], image[i][5], image[i][6], image[i][7], image[i][8], image[i][9]);
}
void printInfo(int * info){
    printf("-----------------------------------------------\n");
    printf("X=[%d], Y=[%d], width=[%d], height=[%d]\n", info[0], info[1], info[2], info[3]);
}
