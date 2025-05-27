# 24542 튜터 튜티
import sys

input= sys.stdin.readline
num = 1000000007

N,M = map(int,input().split())
students = []

for _ in range(M):
    u,v = (map(int, input().split()))
    u,v = sorted((u,v))
    students.append((u,v))
dic = {}

for u,v in students:
    if u not in dic:
        dic[u] = []
    dic[u].append(v)
    
for u,v in dic.items():
    for i in v:
        if i in dic:
            value = True
    result *= (len(v) + 1)

if value:
    print((result - 1)%num)
else:
    print(result%num)