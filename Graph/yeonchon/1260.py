import sys
from collections import deque # 양쪽 끝에서 추가 제거 가능

def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            
            # 정점 번호가 작은 것을 먼저 방문
            for nextNode in reversed(graph[node]):
                stack.append(nextNode)
    print()        

def bfs(graph, start):
    visited = set()
    visited.add(start)
    queue = deque([start])
    
    while queue:
        node = queue.popleft() # 맨 앞 값 제거 후 반환
        print(node, end=" ")
        
        for nextNode in graph[node]:
            if nextNode not in visited:
                visited.add(nextNode) # 방문 set 에 추가
                queue.append(nextNode) # 맨 뒤에 추가


v, e, start = map(int, sys.stdin.readline().strip().split())

# 그래프 초기화
graph = {i: [] for i in range(1, v + 1)}

for i in range(e):
    
    a, b = map(int, sys.stdin.readline().strip().split())
    
    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()
        
    graph[a].append(b)
    graph[b].append(a)

for edgeList in graph.values():
    edgeList.sort()

dfs(graph, start)
bfs(graph, start)
