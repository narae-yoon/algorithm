# µ¿Àü 0 (https://www.acmicpc.net/problem/11047)

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 0

for i in range(1, N+1):
  coin_value = A[N-i]
  if (coin_value <= K):
    cnt += K // coin_value
    K %= coin_value

print(cnt)