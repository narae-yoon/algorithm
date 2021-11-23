# 배열의 모든 왼쪽 값은 자신의 값보다 작고, 모든 오른쪽 값은 자신의값보다 큰 항목 찾기

def find_element(arr):
  n = len(arr)
  leftMax = [0 for i in range(n)]
  leftMax[0] = float('-inf')
  rightMin = float('inf')

  for i in range(1, n):
    if leftMax[i-1] > arr[i-1]: 
      leftMax[i] = leftMax[i-1]
    else: 
      leftMax[i] = arr[i-1]
  
  for i in range(n-1, -1, -1):
    if leftMax[i] < arr[i] < rightMin:
      return i
    if rightMin > arr[i]:
      rightMin = arr[i]
    
  return -1


arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
print(find_element(arr))