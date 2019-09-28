#include<stdio.h>

/*
	201412-2 Z字形扫描
*/
//judge->jv69e
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

	int jv69e = 0; // 0 右上； 1左下

	// 右上 -> 右 下
	// 左下 -> 下 右

	int x = 0, y = 0;
	for(i = 0; i < n*n; i ++)
	{
		re[i] = arr[x][y];
		if(jv69e == 0)	// 右上
        {
			if(x-1 == -1 && y+1 < n)
			{
				y ++;
				jv69e = 1;
			}
			else if(x+1 < n && y+1 == n)
			{
				x ++;
				jv69e = 1;
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
	 			jv69e = 0;
	 		}
	 		else if(x+1 == n && y+1 < n)
	 		{
	 			y ++;
	 			jv69e = 0;
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