import sys

input = sys.stdin.readline

N, M = map(int,input().split())
# print(N, M)

num_list = list(map(int, input().split()))
dp = [0] * (N)
dp[0] = num_list[0]
# print(dp)
# print(num_list)

for i in range(1, N):
    dp[i] = dp[i-1] + num_list[i] 
# print(dp)

for _ in range(M):
    i, j = (map(int, input().split()))
    # print(i, j)
        
    if i==j:
        print(num_list[i-1])
    else:
        if i==1:
            print(dp[j-1])
        else:
            print(dp[j-1]-dp[i-2])