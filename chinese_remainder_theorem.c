#include <stdio.h>

long long extendedEuclidean(long long a, long long b, long long *x, long long *y) {
    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }
    long long x1, y1;
    long long gcd = extendedEuclidean(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;
    return gcd;
}

long long modInverse(long long a, long long m) {
    long long x, y;
    long long g = extendedEuclidean(a, m, &x, &y);
    if (g != 1) {
        printf("Inverse doesn't exist");
        return -1;
    }
    return (x % m + m) % m;
}

long long chineseRemainderTheorem(long long num[], long long rem[], int k) {
    long long prod = 1;
    for (int i = 0; i < k; i++) {
        prod *= num[i];
    }

    long long result = 0;
    for (int i = 0; i < k; i++) {
        long long pp = prod / num[i];
        result += rem[i] * modInverse(pp, num[i]) * pp;
    }

    return (result % prod + prod) % prod;
}

int main() {
    long long num[] = {3, 4, 5};
    long long rem[] = {2, 3, 1};
    int k = sizeof(num) / sizeof(num[0]);

    printf("The solution is: %lld\n", chineseRemainderTheorem(num, rem, k));

    return 0;
}