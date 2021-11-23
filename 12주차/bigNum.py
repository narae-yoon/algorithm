# 연결하여 만들 수 있는 가장 큰 수 찾기 프로그램

def solution(numbers):
  answer = ''
  max_len = len(str(max(numbers)))
  
  for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
  
  numbers.sort(key = lambda x : x * max_len, reverse = True)
  
  for i in range(len(numbers)):
    answer += numbers[i]
  
  if answer < '1':
    answer = '0'
  
  return answer
    
numbers = ["10","68","75","7","21","12"]
print(solution(numbers))