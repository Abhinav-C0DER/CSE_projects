#include <stdio.h>

int gcd(int a, int b) {
    while (b) {
        a %= b;
        int temp = a;
        a = b;
        b = temp;
    }
    return a;
}

int order_mod(int a, int n) {
    if (n == 1) {
        return 1;
    }

    if (gcd(a, n) != 1) {
        return 0;
    }

    long long power = a % n;

    for (int k = 1; k < n; k++) {
        if (power == 1) {
            return k;
        }
        power = (power * a) % n;
    }

    return 0;
}

int main() {
    int a, n;

    printf("Enter the base (a): ");
    scanf("%d", &a);

    printf("Enter the modulus (n): ");
    scanf("%d", &n);

    int result = order_mod(a, n);

    if (result == 0) {
        printf("\nThe order is undefined because %d and %d are not coprime.\n", a, n);
    } else {
        printf("\norder_mod(%d, %d) = %d\n", a, n, result);
    }

    return 0;
}