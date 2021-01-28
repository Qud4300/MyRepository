#include <stdio.h>

int main(void)
{
    int in;
    char grade;
    scanf("%d", &in);
    
    if(in>=90 && in<=100)
        grade = 'A';
    else if(in>=80 && in<90)
        grade = 'B';
    else if(in>=70 && in<80)
        grade = 'C';
    else if(in>=60 && in<70)
        grade = 'D';
    else
        grade = 'F';
    
    printf("%c", grade);
    return 0;
}