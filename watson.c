
#include <stdio.h>
#include <string.h>

int main(){
    char s[1000];
    scanf("%s", s);

    int finalEq = 0;

    for (int i = 0; i < strlen(s); i++){
        if(s[i] >= '0' && s[i] <= '9'){
            finalEq = finalEq + (s[i] - '0');
            i++;}
        else if(strncmp(&s[i], "minus", 5) == 0){
            finalEq = finalEq - (s[i+5] - '0');
            i = i + 5;}
        else if(strncmp(&s[i], "plus", 4) == 0){
            finalEq = finalEq + (s[i+4] - '0');
            i = i + 4;}
        else if(strncmp(&s[i], "times", 5) == 0){
            finalEq = finalEq * (s[i+5] - '0');
            i = i + 5;}
        else{
            finalEq = s[i] * s[i+13];}
    }
    printf("%d", finalEq);
}

