# include "stdio.h"
# include <iostream>
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
        int s1,s2,sum;

	s1=func_A();
	s2=func_B();
    sum=s1+s2;
	int a, b;
	//printf("[INFO] This is a program for solving B��zout's lemma\n");
	//printf("[INFO] Put in two numbers divided with a space\n");
	int* r = (int*)calloc(512, sizeof(int));
	int* q = (int*)calloc(512, sizeof(int));
	int* s = (int*)calloc(512, sizeof(int));
	scanf_s("%d %d", &a, &b);
	if (a == 0 && b == 0)
	{
		perror("Illigal input!\n");
		return 0;
	}
	if (a >= b)
	{
		r[0] = a;
		r[1] = b;
	}
	else
	{
		r[0] = b;
		r[1] = a;
	}
	int i, j;
	for (i = 0; r[i + 1] != 0; i++)
	{
		r[i + 2] = r[i] % r[i + 1];
		q[i + 1] = r[i] / r[i + 1];//Q start with 1
		printf("[INFO] r%d=r%dq%d+r%d:%d=%d*%d+%d\n", i, i + 1, i + 1, i + 2, r[i], r[i + 1], q[i + 1], r[i + 2]);
	}
	printf("[SUCCESS] gcd(a,b)=%d\n", r[i]);
	system("PAUSE");
	int n = i + 1;//Save parameter n
	printf("[INFO] n=%d\n", n);
	/*Calculate S*/
	s[0] = 0;
	s[1] = 1;
	for (i = 0; (n - 2 - i) > 0; i++)
	{
		s[i + 2] = s[i] - (s[i + 1] * q[n - 2 - i]);
		printf("[INFO] S%d=S%d-(S%d*q%d):%d=%d-(%d*%d)\n", i + 2, i, i + 1, n - 2 - i, s[i + 2], s[i], s[i + 1], q[n - 2 - i]);
	}
	printf("[SUCCESS] %d*%d+%d*%d=%d\n", a, s[n - 2], b, s[n - 1], r[n - 1]);
	system("PAUSE");
	return 0;
}