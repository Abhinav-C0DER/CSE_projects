#include <stdio.h>

int is_quadratic_residue(int a, int p){
    int r = a % p;
    
    if (r < 0) {
        r += p;
    }

    for(int i = 0; i < p; i++){
        if((i * i) % p == r){
            return 1; 
        }
    }
    return 0; 
}

int main(void){
    int a, p;
    printf("Enter a: ");
    scanf("%d", &a);
    printf("Enter p (prime): ");
    scanf("%d", &p);

    int result = is_quadratic_residue(a, p);

    if(result == 1) {
        printf("\nResult: %d is a quadratic residue modulo %d.\n", a, p);
    } else {
        printf("\nResult: %d is NOT a quadratic residue modulo %d.\n", a, p);
    }
    
    return 0; 
}