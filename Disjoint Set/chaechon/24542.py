# 24542 튜터 튜티
# 포레스트니까 그래프..

import sys
from collections import deque

input = sys.stdin.readline
num = 1000000007

N,M = map(int,input().split())
students = {}
result = 1
visited = [0] * (N+1)

def bfs(i):
    queue = deque()
    queue.append(i)
    size = 1
    
    visited[i] = 1
    
    while queue:
        x = queue.popleft()
        for student in students.get(x, []):
            # 연결 확인
            if visited[student] == 0:
                queue.append(student)
                visited[student] = 1
                size +=1
    
    return size
                 

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
        node = bfs(i)
        # 노드의 수 곱하기
        result *= node
        result %= num

print(result)