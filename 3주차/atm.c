// ATM (https://www.acmicpc.net/problem/11399)

#include <stdio.h>
int main (void) {
  int N, i, j;
  int P[1000];
  int waitTime = 0, totTime = 0;
  
  scanf("%d", &N);
  
  for (i = 0; i < N; i++) {
    scanf("%d", &P[i]);
  }

  for (i = 0; i < N; i++) {
    for (j = 0; j < N-(i+1); j++) {
      if (P[j] > P[j+1]) {
        int temp;
        temp = P[j];
        P[j] = P[j+1];
        P[j+1] = temp;
      }
    }
  }

  for(i = 0; i < N; i++) {
    waitTime += P[i];
    totTime += waitTime;
  }

  printf("%d", totTime);

  return 0;
}