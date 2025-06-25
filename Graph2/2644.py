import sys
from collections import deque

input = sys.stdin.readline

def bfs(end, count):
    visited = {start}
    queue = deque([(start, count)])
    
    while queue:
        # print(queue, "count = ", count)
        node = queue.popleft()
        flag = False
        # print(node)
        
        if node[0] == end:
            return node[1]
        
        for nextNode in graph[node[0]]:
            if nextNode not in visited:
                flag = True
                queue.append((nextNode, count+1))
                visited.add(node[0])
        if flag:
            count += 1
    return -1
        
n = int(input().rstrip())
start, end = map(int, input().rstrip().split())
m = int(input().rstrip())

graph = {i: [] for i in range(1, n+1)}


for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x) # 양방향
    
print(bfs(end, 0))
    