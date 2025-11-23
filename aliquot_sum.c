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
    int num, result;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    result = alquit_sum(num);
    printf("The sum of all divisors of %d is: %d\n", num, result);
    return 0;
}