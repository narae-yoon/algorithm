// µ¿Àü 0 (https://www.acmicpc.net/problem/11047)
#include <stdio.h>
int main (void) {
  int N, K;
  int i, cnt = 0;
  int A[10];
  
  scanf("%d %d", &N, &K);
  
  for (i = 0; i < N; i++) {
    scanf("%d", &A[i]);
  }

  for (i = N-1; i >= 0; i--) {
    if (A[i] <= K) {
      cnt += K / A[i];
      K %= A[i];
    }
  }

  printf("%d", cnt);

  return 0;
}