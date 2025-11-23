#include<stdio.h>
int alquit_sum(int x){
        int sum=0, i;
        for (i=1;i<x;i++){
            if (x%i==0){
                sum+=i;
            }
        }
    return sum;
    }
 int main(void){
    int num1, result1, num2, result2;
    printf("Enter 1st positive integer: ");
    scanf("%d", &num1);
    printf("Enter 2nd positive integer: ");
    scanf("%d", &num2);
    
    result1 = alquit_sum(num1);
    result2 = alquit_sum(num2);
    printf("The sum of all divisors of %d is: %d\n", num1, result1);
    printf("The sum of all divisors of %d is: %d\n", num2, result2);
    if (result1 == result2){
        printf("%d and %d are amicable numbers.\n", num1, num2);
    }
    else{
        printf("%d and %d are not amicable numbers.\n", num1, num2);
    }
    return 0;

}