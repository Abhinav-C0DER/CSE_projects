#include <stdio.h>
#include <stdlib.h>

int mod_inverse(int a, int m) {
    if (m == 1)
        return 0;
    int m0 = m;
    int t, q;
    int x0 = 0, x1 = 1;
    int a_orig = a;
    while (m > 0) {
        q = a / m;
        t = m;
        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (a != 1) {
        printf("Error: Inverse does not exist for %d mod %d (GCD is %d)\n", a_orig, m0, a);
        exit(1);
    }

    if (x1 < 0)
        x1 += m0;

    return x1;
}

int main(void) {
    int a, m;
    printf("Enter a number (a): ");
    scanf("%d", &a);
    printf("Enter modulus (m): ");
    scanf("%d", &m);

    if (m <= 0) {
        printf("Error: Modulus must be greater than 0.\n");
        return 1;
    }

    int result = mod_inverse(a, m);
    printf("Modular Inverse: %d\n", result);
    return 0;
}