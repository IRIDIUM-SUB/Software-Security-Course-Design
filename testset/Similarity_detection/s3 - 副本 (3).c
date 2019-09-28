#include<stdio.h>

/*
	201412-2 Z字形扫描
*/
//x->sub1,y->sub2
#define SIZE 510
int arr[SIZE][SIZE];
int re[SIZE*SIZE];
int func_A()
{
    return 1;
}
int func_B()
{
    return 2;
}
int main()
{
//	freopen("input.txt", "r", stdin);

	int n;
	int a,b,c;
	scanf("%d", &n);
	a=func_A();
	b=func_B();
    c=a+b;
	int i, j;
	for(i = 0; i < n; i ++)
	{
		for(j = 0; j < n; j ++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	int judge = 0; // 0 右上； 1左下

	// 右上 -> 右 下
	// 左下 -> 下 右

	int sub1 = 0, sub2 = 0;
	for(i = 0; i < n*n; i ++)
	{
		re[i] = arr[sub1][sub2];
		if(judge == 0)	// 右上
        {
			if(sub1-1 == -1 && sub2+1 < n)
			{
				sub2 ++;
				judge = 1;
			}
			else if(sub1+1 < n && sub2+1 == n)
			{
				sub1 ++;
				judge = 1;
			}
			else
			{
				sub1 --;
				sub2 ++;
			}

	 	}
	 	else	// 左下
	 	{
	 		if(sub1+1 < n && sub2-1 == -1)
			{
	 			sub1 ++;
	 			judge = 0;
	 		}
	 		else if(sub1+1 == n && sub2+1 < n)
	 		{
	 			sub2 ++;
	 			judge = 0;
	 		}
	 		else
	 		{
	 			sub1 ++;
				sub2 --;
	 		}

	 	}
	}


	for(i = 0; i < n*n; i ++)
	{
		printf("%d ", re[i]);
	}

	return 0;
}