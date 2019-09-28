#include <stdio.h>
int main(int argc,char* argv){
    char *A= malloc(10);
    char *B= malloc(8);
    char *C= malloc(4);
    strcpy(B,"BBBBBBBB");
    strcpy(C,"CCCC");
    strcpy(A,"SSSSSSSSSSS");

    return 0;
}