# 24542 튜터 튜티
# 포레스트니까 그래프..

import sys

input= sys.stdin.readline
num = 1000000007

N,M = map(int,input().split())
students = []

for _ in range(M):
    u,v = (map(int, input().split()))
    students.append((u,v))
