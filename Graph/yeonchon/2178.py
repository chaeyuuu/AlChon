import sys
from collections import deque

def bfs(graph, endX, endY):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        if x == endX and y == endY:
            print(graph[x][y])
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
                
row, col = map(int, sys.stdin.readline().strip().split())

graph = []

for _ in range(row):
    # 입력 string 쪼개기
    graph.append([int(char) for char in sys.stdin.readline().strip()])
    
bfs(graph, row - 1, col - 1)