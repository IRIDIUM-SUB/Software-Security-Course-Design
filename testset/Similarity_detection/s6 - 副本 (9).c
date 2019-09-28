#include "stdio.h"
#include "malloc.h"

//CFG
//has been modified and need to change format
#define TRUE 1
#define FALSE -1
#define OK 1
#define ERROR 0
#define OVERFLOW 0
#define LIST_INIT_SIZE 255;

int cho;
int sta;
int aim;
int dgl;
int* e;
int func_A()
{
    return 1;
}
int func_B()
{
    return 2;
}

typedef int status;
typedef struct list{  //顺序表（顺序结构）的定义
	int * elem;
	int length;
	int listsize;
}SqList;

int IntiaList(SqList * L)
{
 L->elem=(int*)malloc(255*sizeof(int));
 if(!(L->elem))exit(OVERFLOW); //存储分配失败
 L->length=0;  //利用表长为0进行初始化
 L->listsize=255; //容量为LIST_INIT_SIZE
 return 1;
}

status DestroyList(SqList * L)
{
    if(L->listsize==0)//线性表不存在时
    return ERROR;
    if(L->listsize!=0)
	{
		free(L->elem); //释放头结点
	    L->elem=NULL;
     	L->length=0;//表长和容量都设置为0
	    L->listsize=0;
	    return OK;
	}
}

status ClearList(SqList *L)
{
    if(L->listsize==0)//线性表不存在时
    return ERROR;
    if(L->listsize!=0)
	{
	L->length=0; //表长设置为0对表进行重置
	L->listsize=LIST_INIT_SIZE;//容量不变
	return OK;
	}
}

status ListEmpty(SqList L)
{
    if(L.listsize==0)//线性表不存在时
    return ERROR;
     if(L.listsize!=0)
	{
	 if(L.length==0)//直接用表长来判断是否为空表
	 {
	 return TRUE;}
	 else
	 return FALSE;
    }
}

int ListLength(SqList L)
{
	if(L.listsize==0)//线性表不存在时
    return ERROR;
    if(L.listsize!=0)//直接返回表长 error赋值为-1 防止与表长为0时弄混
    return L.length;
}

status GetElem(SqList L,int i,int* e)
{
	if(L.listsize==0)//线性表不存在时
    return ERROR;
    if(L.listsize!=0)
	{
	if(i<1||i>L.length)  //i值不合法
	return ERROR;
	*e=*(L.elem+(i-1));

	printf("%d\n",*e); //用e返回要找值
	return OK;
    }
}

status LocateElem(SqList L,int e)
{
    int i;
    if(L.listsize==0)//线性表不存在时
    return ERROR;
    if(L.listsize!=0)
    {
      for(i=0;i<L.length;i++)
	{
	  if(L.elem[i]==e)
      return i+1;
      if(i==(L.length-1))
      return ERROR;
	}
	}
}

status PriorElem(SqList L,int cur,int* pre_e)
{
	int j;
	if(L.listsize==0)//线性表不存在时
    return ERROR;
    if(L.listsize!=0)
    {
     for(j=1;j<L.length;j++)//第一个元素没有前驱
	{
	 if((L.elem[j])==cur)
	 {
	  *pre_e=*(L.elem+(j-1));
	  return OK;
     }
    }
	}
	return ERROR;
}

status NextElem(SqList L,int cur,int* next_e)
{
	int j;
	if(L.listsize==0)//线性表不存在时
    return ERROR;
    if(L.listsize!=0)
    {
     for(j=0;j<L.length-1;j++)//最后一个元素没有后驱
	    {
	        if((L.elem[j])==cur)
	        {
	            *next_e=*(L.elem+(j+1));
	            return OK;
	        }
        }
	}
    next_e=NULL;
    return ERROR;
}

status ListInsert(SqList * L,int i,int e)
{   if(L->listsize==0)//线性表不存在时
    return ERROR;
    if(L->listsize!=0)
    {
    int *p,*q;
	if(i<1||i>L->length+1) return ERROR; //i值不合法
	if(L->length>=L->listsize)
	{

		L->elem=(int*)realloc(L->elem,(L->listsize+10)*sizeof(int));//当线性表满时 要额外分配存储
		if(!(L->elem)) exit(OVERFLOW);//存储分配失败
		L->listsize+=10; //存储分配成功 表容量+10
	}
	q=&(L->elem[i-1]);   //q为插入位置
	for(p=&(L->elem[L->length-1]);p>=q;--p)
	*(p+1)=*p; //插入位置及之后的元素右移
	*q=e;//????? //插入e
	++L->length; //表长+1
	return OK;
	}
}

status ListDelete(SqList * L,int i,int* e)
{   if(L->listsize==0)//线性表不存在时
    return ERROR;
    if(L->listsize!=0)
    {
    int *p,*q;
	if(i<1||i>L->length) return ERROR; //i值不合法
	p=L->elem+(i-1); //p为被删除元素的位置
	*e=*p; //e返回被删除的元素的值
	printf("%d\n",*e);
	q=L->elem+L->length-1; //表尾元素的位置
	for(++p;p<=q;++p)
	*(p-1)=*p; //被删除元素之后的元素左移
	--L->length; //表长-1
	return OK;
	}
}

status ListTraverse(SqList L)
{   if(L.listsize==0)//线性表不存在时
    return ERROR;
   if(L.listsize!=0)
   {
   	int i;
   for(i=0;i<L.length;i++)
   printf("%d\n",L.elem[i]);//遍历输出表中的各个元素
   return L.length;
   }
}

int main()

{
     int s1,s2,sum;


    int temp;
printf("this is a test text\n");
printf("sys.\n");
SqList* L;
L=(SqList*)malloc(sizeof(SqList));
L->elem=NULL;
L->length=0;
L->listsize=255;
e=(int*)malloc(sizeof(int));
FILE* fp;
char ch;

if(!IntiaList(L))
	printf("list load failed\n");
else
{//file load part
if ((fp=fopen("test.txt","r"))==NULL)
	{
	 printf("File open error\n ");
	 getchar();
	 return 1;
	}
printf("file has been detected\n");
ch=fgetc(fp);
  if(ch==EOF)
   printf("empty file\n");
  else
   printf("not empty\n");

if(ch!=EOF)
{printf("file is not empty.ues file data or setup a new one?\n0.setup a new one\t1.use directly\n");
scanf("%d",&temp);
if(!temp)
{goto setup;}
else
{fp=fopen("test.txt","r");while(fread(&L->elem[L->length],sizeof(int),1,fp))
   L->length++;
   goto load;
}
}
	setup:
	printf("data load success\n");
	getchar();


	printf("load data temperily: put in data and press 255 to end\n");
	for(;temp!=255;*(L->elem+L->length)=temp,L->length++)
	scanf("%d",&temp);
	L->length--;
	load:
	printf("%d\n",L->length);
	printf("%d\n",L->listsize);
	ListTraverse(*L);
	getchar();getchar();
	//this area is just for temp test about the functions,should be covered after debugging.
	do{
		system("cls");
		printf("\n\n");
        printf("      Menu for Linear Table On Sequence Structure \n");
        printf("-------------------------------------------------\n");
        printf("          1. IntiaList       7. LocateElem\n");
        printf("          2. DestroyList     8. PriorElem\n");
        printf("          3. ClearList       9. NextElem \n");
        printf("          4. ListEmpty     10. ListInsert\n");
        printf("          5. ListLength     11. ListDelete\n");
        printf("          6. GetElem       12. ListTrabverse\n");
        printf("          0. Exit\n");
        printf("-------------------------------------------------\n");
        printf("    celect the operaction number[0~12]:");
        scanf("%d",&cho);
	switch(cho)
	{
	case 1:printf("list has been set up before!\n");getchar();getchar();break;

	case 2:if(!DestroyList(L))
	{printf("list not exist\n");getchar();getchar();break;}
	else
	printf("release success\n");
	ListTraverse(*L);
	getchar();getchar();break;

	case 3:if(!ClearList(L))
	{printf("list not exist\n");getchar();getchar();break;}
	else
	printf("clear success\n");
	ListTraverse(*L);
	getchar();getchar();break;

	case 4:
	sta=ListEmpty(*L);
	if(!sta)
		{printf("list not exist\n");getchar();getchar();break;}
	else
		{if(sta==1)
			printf("list is empty\n");
		else
			printf("not empty\n");}
	getchar();getchar();break;

	case 5:
	if(sta=ListLength(*L))
		{printf("the lenth is %d",sta);}
	else
		printf("list not exist\n");
	getchar();getchar();break;

	case 6:
	printf("put in order\n");
	scanf("%d",&aim);
	if(GetElem(*L,aim,e))
	printf("item needed is %d\n",*e);
	else
	printf("List not exist or order is out of range\n");
	getchar();getchar();break;

	case 7:
	printf("put in data\n");
	scanf("%d",&aim);
	if(sta=LocateElem(*L,aim))
	{printf("find:order is %d",sta);}
	else
	printf("List not exist or data not find\n");
	getchar();getchar();break;

	case 8:
	printf("put in data:");
	scanf("%d",&aim);
	if(PriorElem(*L,aim,e))
	{printf("the prev is %d",*e);}
	else
	printf("List not exist or data not find or out of range\n");
	getchar();getchar();break;

	case 9:
	printf("put in data:");
	scanf("%d",&aim);
	if(NextElem(*L,aim,e))
	{printf("the next is %d",*e);}
	else
	printf("List not exist or data not find or out of range\n");
	getchar();getchar();break;

	case 10:
	printf("put in data and order wanna insert before\n");
	scanf("%d %d",&aim,&dgl);
	if(ListInsert(L,dgl,aim))
	{printf("insert success:now:\n");
	ListTraverse(*L);}
	else
	printf("failed!\n");
	getchar();getchar();break;

	case 11:
	printf("put in order wanna delete\n");
	scanf("%d",&dgl);
	if(ListDelete(L,dgl,e))
	{printf("delete success:now:\n");
	ListTraverse(*L);
	printf("and data deleted is %d",*e);}
	else
	printf("List not exist or order is out of range\n");
	getchar();getchar();break;

	case 12:
	if(!ListTraverse(*L))
	printf("List not exist\n");
	getchar();getchar();break;

	case 0:
	ListTraverse(*L);
	if ((fp=fopen("test.txt","wt"))==NULL)
	{
	 printf("File open error\n ");
	return 1;
	}
	fwrite(L->elem,sizeof(int),L->length,fp);
	fclose(fp);
	DestroyList(L);
	printf("space released and sys closed\n");break;
	}
	}
	while(cho!=0);
}
	s1=func_A();
	s2=func_B();
    sum=s1+s2;
getchar();getchar();
return 0;}