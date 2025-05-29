import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n,m = map(int, input().split())
parent = []
result = 0

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    
    return parent[x]
    
def union(a,b):
    # 집합이 같으면 사이클 아니면 합치기
    a = find(a)
    b = find(b)
    
    if a == b:
        return False 
    
    parent[b] = a # 합치기
    return True
        

# parent = list(range(n))
for i in range(n):
    parent.append(i)

for i in range(1,m+1):
    a, b = map(int, input().split())
    if result == 0 and union(a,b) == 0:
        result = i

print(result)