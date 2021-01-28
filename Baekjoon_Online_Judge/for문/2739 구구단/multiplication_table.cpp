#include <stdio.h>

int main(void)
{
    int in;
    scanf("%d", &in);
    
    for(int i=1; i<=9; i++)
    {
        printf("%d * %d = %d\n", in, i, in*i);
    }
    return 0;
}