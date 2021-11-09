# Set the rightmost unset bit 
# 가장 오른쪽 0 값의 비트를 1로 바꾼 값 찾기

from math import log2

def get_pos_of_rightmost_set_bit(n) :
  return log2(~n&(n+1)) + 1

def set_rightmost_unset_bit(n) :
  if n == 0 :
    return 1
  
  if n & (n + 1) == 0 :
    return n

  pos = get_pos_of_rightmost_set_bit(n)
  return 1 << int(pos - 1) | n

n = input();
print(set_rightmost_unset_bit(n))