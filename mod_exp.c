#include <stdio.h>
long modular_pow(long base, long exp, long mod) {
	long result = 1;
	base %= mod;
	while (exp > 0) {
		if (exp % 2 == 1)
			result = (result * base) % mod;
		exp /= 2;
		base = (base * base) % mod;
	}
	return result;
}
int main(void){
    long num1, num2, num3, result;
    printf("Enter base: ");
    scanf("%ld", &num1);
    printf("Enter exponent: ");
    scanf("%ld", &num2);
    printf("Enter modulus: ");
    scanf("%ld", &num3);
    result = modular_pow(num1, num2, num3);
    printf("Result: %ld\n", result);
    return 0;
   
}