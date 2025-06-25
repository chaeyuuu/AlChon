import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    visited = {start}
    queue = deque([(start, 0)])
    
    while queue:
        # print(queue)
        node, dist = queue.popleft()
        
        if node == end:
            return dist
        
        for nextNode in graph[node]:
            if nextNode not in visited:
                queue.append((nextNode, dist+1))
                visited.add(nextNode)
    return -1
        
n = int(input().rstrip())
start, end = map(int, input().rstrip().split())
m = int(input().rstrip())

graph = {i: [] for i in range(1, n+1)}


for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x) # 양방향
    
print(bfs(start, end))
    