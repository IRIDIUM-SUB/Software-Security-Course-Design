#include<stdio.h>

/*
	201412-2 Z字形扫描
*/
//n->sub3
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

	int sub3;
	int a,b,c;
	scanf("%d", &sub3);
	a=func_A();
	b=func_B();
    c=a+b;
	int i, j;
	for(i = 0; i < sub3; i ++)
	{
		for(j = 0; j < sub3; j ++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	int judge = 0; // 0 右上； 1左下

	// 右上 -> 右 下
	// 左下 -> 下 右

	int x = 0, y = 0;
	for(i = 0; i < sub3*sub3; i ++)
	{
		re[i] = arr[x][y];
		if(judge == 0)	// 右上
        {
			if(x-1 == -1 && y+1 < sub3)
			{
				y ++;
				judge = 1;
			}
			else if(x+1 < sub3 && y+1 == sub3)
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
	 		if(x+1 < sub3 && y-1 == -1)
			{
	 			x ++;
	 			judge = 0;
	 		}
	 		else if(x+1 == sub3 && y+1 < sub3)
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


	for(i = 0; i < sub3*sub3; i ++)
	{
		printf("%d ", re[i]);
	}

	return 0;
}