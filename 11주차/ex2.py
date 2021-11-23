# 배열의 모든 왼쪽 값은 자신의 값보다 작고, 모든 오른쪽 값은 자신의 값보다 큰 항목 찾기
# 모든 조건에 맞는 원소를 출력하는 (수정본) 프로그램 

def find_element(arr):
  n = len(arr)
  leftMax = [0 for i in range(n)]
  rightMin = [0 for i in range(n)]

  leftMax[0] = float('-inf')
  rightMin[n-1] = float('inf')
  sts = 0

  for i in range(1, n):
    if leftMax[i-1] > arr[i-1]: 
      leftMax[i] = leftMax[i-1]
    else: 
      leftMax[i] = arr[i-1]
  
  for i in range(n-2, -1, -1):
    if rightMin[i+1] > arr[i+1]:
      rightMin[i] = arr[i+1]
    else:
      rightMin[i] = rightMin[i+1]
    
  for i in range(n):
    if leftMax[i] < arr[i] < rightMin[i]:
      print(i)
      sts = 1

  if sts == 0:
    print(-1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
find_element(arr)