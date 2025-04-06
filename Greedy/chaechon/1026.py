# 보물

import sys

input = sys.stdin.readline

N = int(input())
A, B = [], []
result = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))
    
A.sort()
B.sort(reverse=True)

for i in range(N):
    result += A[i] * B[i]
    
print(result)