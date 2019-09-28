#include "stdio.h"
#include "stdlib.h"
#include "string.h"
//string->str1n9
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
    int a,b,c;

	a=func_A();
	b=func_B();
    c=a+b;
start:
	char* str1n9;
	char* backup;
	int i, j;
	int size = 512;
	printf("This tool's buffer's size is set 512 as default.Wanna expand?\n");
	int choice;
	printf("1.Y\t0.N\n");
	scanf_s("%d", &choice);
	system("cls");
	if (choice == 1)
	{
		printf("Put in size wanna change\n");
		scanf_s("%d", &size);
		printf("Size expand successfully!\n");
	}
	else if (choice != 0)
	{
		printf("Input Error!\n");
		system("Pause");
		system("cls");
		goto start;
	}
	str1n9 = (char*)malloc(sizeof(char)*size);
	backup = (char*)malloc(sizeof(char)*size);
	if (str1n9 == NULL || backup == NULL)
	{
		printf("Malloc Error\n");
		system("Pause");
		goto start;
	}
	else
	{
		printf("Malloc Successfully: Current size:%d\n", size);
	}
	system("cls");
	printf("Get ready to input str1n9\n");
	printf("str1n9:");
	scanf_s("%s", str1n9, size);
	//gets_s(str1n9, size);
	printf("Comfirm:");
	puts(str1n9);
	strcpy_s(backup, strlen(str1n9) + 1, str1n9);
	system("pause");
chooo:
	printf("Encode or Decode?\n0.E\t1.D\n");
	scanf_s("%d", &choice);
	system("cls");
	if (choice == 1)
	{
		printf("Get ready to Decode...\n");
		system("pause");
		printf("-------------------------------\n");
		for (i = 1; i < 26; i++)
		{
			for (j = 0; str1n9[j] != '\0'&&j < (int)strlen(str1n9); j++)
			{
				if (str1n9[j] == 'a')
				{
					str1n9[j] = 'z';
					continue;
				}
				else if (str1n9[j] == 'A')
				{
					str1n9[j] = 'Z';
					continue;
				}
				str1n9[j]--;
			}

			printf("%d\t%s\n", i, str1n9);
		}
		printf("Decode finished.\n");
		system("pause");
	}
	else if (choice == 0)
	{
		printf("Get ready to Encode...\n");
		system("pause");
		printf("-------------------------------\n");
		for (i = 1; i < 26; i++)
		{
			for (j = 0; str1n9[j] != '\0'&&j < (int)strlen(str1n9); j++)
			{
				if (str1n9[j] == 'z')
				{
					str1n9[j] = 'a';
					continue;
				}
				else if (str1n9[j] == 'Z')
				{
					str1n9[j] = 'A';
					continue;
				}
				str1n9[j]++;
			}

			printf("%d\t%s\n", i, str1n9);
		}
		printf("Encode finished.\n");
		system("pause");
	}
	else
	{
		printf("Input Error!\n");
		system("Pause");
		system("cls");
		goto chooo;
	}
	system("cls");
	printf("Process finished.\n");
	return 0;
}