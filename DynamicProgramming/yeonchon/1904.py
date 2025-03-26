# 1: 1
# 2: 00, 11
# 3: 001, 111, 100

# 5자리의 수열을 만들때, 4개일때 1개짜리 이어붙이기 and 3개일때 2개짜리 이어붙이기 두 경우 존재

# n-1 까지 수열이 채워진 경우, 맨뒤에 1 채우기만 가능
# n-2 까지 수열이 채워진 경우, 맨뒤에 00, 11 채우기가 가능하지만, 11의 경우는 n-1과 겹친다.

# 즉, n 자리 수열의 경우의 수는,
# (n-1 까지의 가능한 수열에 1붙인거 + n-2 까지의 가능한 수열에 00 붙인거)
# 즉 걍 nList[n-1] + nList[n-2] 해주면 됨~

def dp(n):
    # 리스트의 값 채우기 (bottom-up)
    for i in range(3, n):
        nList[i] = (nList[i-1] + nList[i-2]) % 15746 # 나누고 넣어야함
        
    # n-1까지 list 의 값이 채워졌을때,
    return (nList[n-1] + nList[n-2]) % 15746

import sys

n = int(sys.stdin.readline().strip())

if n == 1 or n == 2:
    print(n)
    exit()
    
nList = [0] * (n + 1) # 0일때는 경우의 수 0, 1일때는 경우의 수 1, 2일땐 2
nList[1] = 1
nList[2] = 2

print(dp(n))
