# Toggle case of a string using Bitwise Operators 
# 비트 연산을 통해 문자의 대소문자 바꾸기

def toggle_case(origin_str) :
  toggle_str = ''
  for c in origin_str:
    c = chr(ord(c) ^ 32)
    toggle_str += c

  return toggle_str;

origin_str = input()

print("Toggle case: ", toggle_case(origin_str))

result = toggle_case(origin_str)
print("Original string: ", toggle_case(result))