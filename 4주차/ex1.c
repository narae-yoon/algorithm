// 배열 값 중 0을 찾아 배열 뒤로 배치시키기

#include <stdio.h>
int main(void) {
  int arr1[] = { 2, 3, 0, 0, 4, 0, 6 };
  int n = sizeof(arr1) / sizeof(arr1[0]);
  int j = 0;
  
  for (int i = 0; i < n; i++) {
    if (arr1[i] != 0) {
      arr1[j] = arr1[i];
      j = j + 1;
    }
  }

  for (int i = j; i < n; i++)
    arr1[i] = 0;

  for (int i = 0; i < n; i++)
    printf("%d ", arr1[i]);
  
  return 0;
}