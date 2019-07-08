#include <stdio.h>
int main()
{
int num,m,n;
scanf("%d %d",&m,&n);
for (num = m+1; num <=n-1; num++)
{
 if (num % 2 == 1)
 printf ("%d ", num);
}
return 0;                
}
