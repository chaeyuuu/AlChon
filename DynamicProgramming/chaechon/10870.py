import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * max(2,n+1)
dp[1] = 1

if n == 0:
    print(0)
else:
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp[-1])