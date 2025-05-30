# 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
count = 0
for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in range(N+1):
    if K == 0:
        break
    
for j in coin:
    if K >= j:
        temp = K//j
        count += temp
        K -= temp*j
    
print(count)