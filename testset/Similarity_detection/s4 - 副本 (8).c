#include "stdio.h"
#include "stdlib.h"
#include "string.h"
//CFG:Orstring/backup's declaration
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
	char* string;
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
		string = (char*)malloc(sizeof(char)*size);
		backup = (char*)malloc(sizeof(char)*size);
	}
	else if (choice != 0)
	{
		printf("Input Error!\n");
		system("Pause");
		system("cls");
		goto start;
	}

	if (string == NULL || backup == NULL)
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
	printf("Get ready to input string\n");
	printf("string:");
	scanf_s("%s", string, size);
	//gets_s(string, size);
	printf("Comfirm:");
	puts(string);
	strcpy_s(backup, strlen(string) + 1, string);
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
			for (j = 0; string[j] != '\0'&&j < (int)strlen(string); j++)
			{
				if (string[j] == 'a')
				{
					string[j] = 'z';
					continue;
				}
				else if (string[j] == 'A')
				{
					string[j] = 'Z';
					continue;
				}
				string[j]--;
			}

			printf("%d\t%s\n", i, string);
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
			for (j = 0; string[j] != '\0'&&j < (int)strlen(string); j++)
			{
				if (string[j] == 'z')
				{
					string[j] = 'a';
					continue;
				}
				else if (string[j] == 'Z')
				{
					string[j] = 'A';
					continue;
				}
				string[j]++;
			}

			printf("%d\t%s\n", i, string);
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