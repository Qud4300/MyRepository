#include <stdio.h>

int main(void)
{
    int a,b,c,d,e;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);
    scanf("%d", &e);
    
   if(a<40)
       a=40;
   if(b<40)
       b=40;
   if(c<40)
       c=40;
   if(d<40)
       d=40;
   if(e<40)
       e=40;
   printf("%d", (a+b+c+d+e)/5);
    
    
}