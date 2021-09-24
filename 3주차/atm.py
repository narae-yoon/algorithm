# ATM (https://www.acmicpc.net/problem/11399)

N = int(input())
P = list(map(int, input().split()))
wait_time, tot_time = 0, 0

P.sort()
for i in P:
  wait_time += i
  tot_time += wait_time

print(tot_time)