import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N+1) 

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if N%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if N%2 ==0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[N])
