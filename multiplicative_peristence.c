#include <stdio.h>
 int multiplicative_persistence(int n) {
     int count = 0;
     while (n >= 10) {
         int product = 1;
         while (n > 0) {
             product *= n % 10;
             n /= 10;
         }
         n = product;
         count++;
     }
     return count;
 }

 int main(void){
    int num, result;
      printf("Enter a number: ");
    scanf("%d", &num);
    result = multiplicative_persistence(num);
    printf("Multiplicative persistence of %d is %d\n", num, result);
    return 0;
 }