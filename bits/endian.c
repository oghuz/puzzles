#include <stdio.h>
void print_bytes(const void *object, size_t size)
{
    size_t i;

      printf("[ ");
        for(i = 0; i < size; i++)
            {
                  printf("%02x ", ((const unsigned char *) object)[i] & 0xff);
                    }
          printf("]\n");
}

int main() 
{
   unsigned int i = 1;
   char *c = (char*)&i;

   print_bytes(&i, sizeof(int));

   if (*c)    
       printf("Little endian");
   else
       printf("Big endian");
   return 0;
}

