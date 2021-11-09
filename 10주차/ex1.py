# Check if a Number is Odd or Even using Bitwise Operators 
# 비트 연산을 통해 짝수, 홀수 판별하기

def is_even(n) :
  if n ^ 1 == n + 1 :
    return 1;
  else :
    return 0;

n = int(input())

if is_even(n) == 1 :
  print("Even")
else :
  print("Odd")