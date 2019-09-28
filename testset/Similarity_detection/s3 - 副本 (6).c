#include<stdio.h>

/*
	201412-2 Z字形扫描
*/
//CFG
#define SIZE 510
int arr[SIZE][SIZE];
int re[SIZE*SIZE];
int func_A()
{
    return 1;
}
int func_A()
{
    return 2;
}
int main()
{
//	freopen("input.txt", "r", stdin);

	int n;
	int a,b,c;
	scanf("%d", &n);
	b=func_B();
	a=func_A();

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

	int x = 0, y = 0;
	for(i = 0; i < n*n; i ++)
	{
		re[i] = arr[x][y];
		if(judge == 0)	// 右上
        {
			if(x-1 == -1 && y+1 < n)
			{
				y ++;
				judge = 1;
			}
			else if(x+1 < n && y+1 == n)
			{
				x ++;
				judge = 1;
			}
			else
			{
				x --;
				y ++;
			}

	 	}
	 	else	// 左下
	 	{
	 		if(x+1 < n && y-1 == -1)
			{
	 			x ++;
	 			judge = 0;
	 		}
	 		else if(x+1 == n && y+1 < n)
	 		{
	 			y ++;
	 			judge = 0;
	 		}
	 		else
	 		{
	 			x ++;
				y --;
	 		}

	 	}
	}


	for(i = 0; i < n*n; i ++)
	{
		printf("%d ", re[i]);
	}

	return 0;
}