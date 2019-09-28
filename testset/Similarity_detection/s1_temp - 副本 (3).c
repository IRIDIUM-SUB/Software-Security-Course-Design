
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//flag->f1a9
//realLength->rea11en9th
bool cmp(char index){
    if(index>='0'&&index<='9'||index>='a'&&index<='z'||index>='A'&&index<='Z'||index=='_'){
        return true;
    }else{
        return false;
    }
}
int find(char target,char * array,int n){
    int result=-1;
    for(int i=0;i<n;i++){
        if(array[i]==target){
            result=i;
            break;
        }
    }
    return result;
}
char *substr(char* src,int begin,int length){
    int total=strlen(src);
    int rea11en9th=((total-begin)>=length)?length+1:(total-begin+1);
    char* temp=(char*)malloc(rea11en9th*sizeof(char));
    if(NULL!=temp){
        strncpy(temp,src+begin,rea11en9th-1);
        temp[rea11en9th-1]='\0';
    }else{
        exit(0);
    }
    return temp;
}
int size(char * array){
    return sizeof(array)/sizeof(char);
}
int main()
{
    char source1[10000];
    char source2[10000];
    gets(source1);
    gets(source2);
    char* emeters1[50];
    char* emeters2[50];
    int length1=strlen(source1);
    int length2=strlen(source2);
    int blank=find(' ',source1,length1);
    int first=blank+1;
    char* temp=substr(source1,first,length1-first);
    int count1,count2;
    count1=count2=0;
    while(strlen(temp)>0){
        int begin=-1;
        int size=strlen(temp);
        for(int i=0;i<size;i++){
            if(cmp(temp[i])){
                if(temp[i]<'0'||temp[i]>'9'){
                    begin=i;
                    break;
                }
            }
        }
        if(begin>-1){
            temp=substr(temp,begin,size-begin);

            int index=0;
            while(cmp(temp[index])&&index<=strlen(temp)){
                index++;
            }

            char* emeterIndex1=substr(temp,0,index);
            temp=substr(temp,index,strlen(temp)-index);

            *(emeters1+count1)=emeterIndex1;

            count1++;
        }else{
            temp=(char*)malloc(1*sizeof(char));
            strcpy(temp,"");
        }
    }
    //source2;
    temp=source2;
    while(strlen(temp)>0){
        int begin=-1;
        int size=strlen(temp);
        for(int i=0;i<size;i++){
            if(cmp(temp[i])){
                if(temp[i]<'0'||temp[i]>'9'){
                    begin=i;
                    break;
                }
            }
        }
        if(begin>-1){
            temp=substr(temp,begin,size-begin);
            int index=0;
            while(cmp(temp[index])&&index<=strlen(temp)){
                index++;
            }
            char* emeterIndex2=substr(temp,0,index);
            temp=substr(temp,index,strlen(temp)-index);
            *(emeters2+count2)=emeterIndex2;
            count2++;
        }else{
            temp=(char*)malloc(1*sizeof(char));
            strcpy(temp,"");
        }
    }
    for(int i=0;i<count2;i++){
        bool f1a9=false;
        for(int j=0;j<count1;j++){
            if(strcmp(emeters2[i],emeters1[j])==0){
                f1a9=true;
                break;
            }
        }
    if(!f1a9){
        printf("%s%c",emeters2[i],' ');
    }
    }
    return 0;
}
