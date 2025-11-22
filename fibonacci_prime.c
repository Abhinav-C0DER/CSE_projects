#include <stdio.h>

int is_perfect_square(long long n) {
    if (n < 0) return 0;
    if (n == 0) return 1;
    
    for (long long i = 1; ; ++i) {
        long long square = i * i;
        if (square == n) {
            return 1;
        }
        if (square > n || square < 0) {
            return 0;
        }
    }
}

int is_fibonacci(int n) {
    if (n < 0) return 0;
    long long test1 = 5LL * n * n + 4;
    long long test2 = 5LL * n * n - 4;
    return is_perfect_square(test1) || is_perfect_square(test2);
}

int is_prime(int n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    
    for (int i = 5; i * i <= n; i = i + 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return 0;
        }
    }
    return 1;
}

int is_fibonacci_prime(int n) {
    if (is_prime(n) && is_fibonacci(n)) {
        return 1;
    }
    return 0;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    if (is_fibonacci_prime(n)) {
        printf("\n%d is both a Fibonacci number and a prime number.\n", n);
    } else if (is_prime(n)) {
        printf("\n%d is prime, but NOT a Fibonacci number.\n", n);
    } else if (is_fibonacci(n)) {
        printf("\n%d is a Fibonacci number, but NOT prime.\n", n);
    } else {
        printf("\n%d is NEITHER a Fibonacci number NOR prime.\n", n);
    }
    
    return 0;
}