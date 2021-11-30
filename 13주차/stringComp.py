def solution(s):
  answer = len(s)

  for i in range(1, int(len(s)/2)+1):
    length = len(s)

    for j in range(len(s)):
      z = i
      cnt = 0

      while j + z < len(s):
        if s[j:j+i] == s[j+z:j+z+i]:
          cnt += 1
        else:
          length -= i * cnt
          if cnt:
            length += len(str(cnt+1))
          j += z-1
          break
        
        if j+z+i >= len(s):
          length -= i * cnt
          length += len(str(cnt+1))
          j += z

        z += i 

    if length < answer:
      answer = length

  return answer

s = "abcabcdede"
print(solution(s))
