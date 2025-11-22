#include <stdio.h>
double mean_of_digits(long n){
    int count = 0;
    long sum = 0;
    while (n > 0){
        sum += n % 10;
        n /= 10;
        count++;
    }
    return (double)sum / count;
}
int main(void){
    long n;
    printf("Enter a number: ");
    scanf("%ld", &n);
    printf("Mean of digits: %.2f\n", mean_of_digits(n));
    return 0;
}