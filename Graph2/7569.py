import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global queue, graph
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    dz = [1, -1]
    day = 0
    
    while queue:
        nodeX, nodeY, nodeZ, day = queue.popleft()
        graph[nodeZ][nodeY][nodeX] = 1
        
        for i in range(4):
            nx = nodeX + dx[i]
            ny = nodeY + dy[i]
            
            if (0 <= nx < m) and (0 <= ny < n) and (graph[nodeZ][ny][nx] == 0):
                queue.append((nx, ny, nodeZ, day+1))
                graph[nodeZ][ny][nx] = 1
                
        for j in range(2):
            nz = nodeZ + dz[j]
            
            if (0 <= nz < h) and (graph[nz][nodeY][nodeX] == 0):
                queue.append((nodeX, nodeY, nz, day+1))
                graph[nz][nodeY][nodeX] = 1
                    
    return day

m, n, h = map(int, input().strip().split())
    
graph = [[] for _ in range(h)]

queue = deque([])

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().strip().split())))

for height in range(h):
    for col in range(n):
        for row in range(m):
            if graph[height][col][row] == 1:
                queue.append((row, col, height, 0))
                
answer = bfs()

for height in range(h):
    for col in range(n):
        for row in range(m):
            if graph[height][col][row] == 0: # 토마토가 모두 익지 않은 상황
                print("-1")
                exit()

print(answer)