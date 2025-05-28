# 24542 튜터 튜티
# 포레스트니까 그래프..

import sys

input = sys.stdin.readline
num = 1000000007

N,M = map(int,input().split())
students = {}
result = 1
visited = [0] * (N+1)

def dfs(i):
    visited[i] = 1
    node = 1
    # 연결되어 있는 정점들 확인
    for student in students[i]:
        if visited[student] == 0:
            node += dfs(student)
    return node
    

for _ in range(M):
    u,v = (map(int, input().split()))
    
    if u not in students:
        students[u] = []
    students[u].append(v)
    
    if v not in students:
        students[v] = []
    students[v].append(u)
    
for i in range(1, N+1):
    if visited[i] == 0:
        node = dfs(i)
        # 노드의 수 곱하기
        result *= node
        result %= num

print(result)
        
