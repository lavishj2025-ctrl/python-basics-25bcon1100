#include <stdio.h>
int main() {
    int num;
    int prod = 1;
    printf("Enter the number: ");
    scanf("%d", &num);
    for(int i = 1; i <= num; i++) {
        prod = prod * i;
    }
    printf("The factorial of the number is %d\n", prod);
    return 0;
}