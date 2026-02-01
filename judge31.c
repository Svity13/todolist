#include <stdio.h>

int main() {

    long long n;
    scanf("%lld", &n);
    long long numEq = 0;

    while(numEq * numEq < n){
	numEq++;
    }

    long long difference = (numEq * numEq) - n;
    printf("%lld", difference);
}
