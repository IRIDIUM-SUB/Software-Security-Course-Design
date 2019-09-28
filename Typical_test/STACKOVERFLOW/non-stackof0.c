
// filename: overflow.c
#include <stdio.h>
#include <string.h>

int func()
{	char in[]="kkkkskkkkkkk";
	char buf[10];

	strcpy(buf, in);
	return 0;
}

int main()
{
	char *in = "myinput";
	int ret;

	ret = func();

	return 0;
}
