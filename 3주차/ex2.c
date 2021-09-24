// 문제 2 (곱하기 혹은 더하기)
#include <stdio.h>
#include <string.h>
int main(void) {
  char str[20];
  scanf("%s", str);

  int result = str[0] - '0';

  for (int i = 1; i< strlen(str); i++) {
    int num = str[i] - '0';
    if (num <= 1 || result <= 1) result += num;
    else result *= num;
  }
  
  printf("%d ", result );
}