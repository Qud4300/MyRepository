#include <stdio.h>
#define Self( a ) ( a + a%10 + (a%100)/10 + (a%1000)/100 + (a%10000)/1000 )
int self_function(int num)
{
	int i;
	for (i = 1; i<=num ; i++)
	{
		if ( Self(i) == num )
			return 0;
		else if (i == num)
			return 1;
		else;
	}
}

int main(void)
{
	int i;
	for (i = 1; i <= 10000; i++)
	{
		if (self_function(i) == 1)
			printf("%d\n", i);
		else;
	}
	return 0;
}