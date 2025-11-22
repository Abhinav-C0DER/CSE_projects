#include <stdio.h>

int count_divisors(int n) {
    if (n == 0) {
        return 0; 
    }
    
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            count++;
        }
    }
    return count;
}

int is_highly_composite(int n) {
    if (n <= 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }

    int divisors_of_n = count_divisors(n);

    for (int k = 1; k < n; k++) {
        if (count_divisors(k) >= divisors_of_n) {
            return 0;
        }
    }

    return 1;
}

int main(void) {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    int result = is_highly_composite(num);

    if (result == 1) {
        printf("%d is a highly composite number.\n", num);
    } else {
        printf("%d is NOT a highly composite number.\n", num);
    }

    return 0;
}