#include <stdio.h>
#include <math.h>
 
int main()
{
     int a, d, n;
     int sum = 0;
 
    
             scanf("%d", &n);
     scanf("%d", &a);
     scanf("%d", &d);
     sum = (n * (2 * a + (n - 1)* d ))/ 2;
       
               printf("%d",sum);
     
     return 0;
}
