import sys

# 처음 두 수를 알기 때문에 bottom-up으로 풀 수 있다.
def calculator(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1) # 현재 i가 되기 위한 연산 수와, i//2 까지의 연산 수 + 1 중에 더 작은 값
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)


n = int(sys.stdin.readline().strip())
dp = [0] * (n + 1) # 0이 n+1개 있는 리스트로 초기화

calculator(n)
print(dp[n])