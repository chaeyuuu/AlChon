# 직사각형 조건
# 1. 마주보는 두 변의 길이가 같음
# .. 

import sys

input = sys.stdin.readline
N = int(input())
nlist, temp = set(), []
result=0

a,b = map(int,input().split())

for _ in range(N):
    x, y = map(int,input().split())
    nlist.add((x,y))
    
for x,y in nlist:
    if (x+a, y) in nlist and (x, y+b) in nlist and (x+a, y+b) in nlist:
        result += 1
    
print(result)