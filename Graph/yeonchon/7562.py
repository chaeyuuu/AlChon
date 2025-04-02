import sys
from collections import deque

def bfs(graph, start, end):
    dx = [1, 2, 2, 1, -1, -2, -1, -2]
    dy = [-2, -1, 1, 2, -2, -1, 2, 1]
    
    queue = deque([(start[0], start[1])])
    
    while queue:
        landX, landY = queue.popleft()
        
        if landX == end[0] and landY == end[1]:
            print(graph[landY][landX])
            return
        
        for i in range(8):
            nx = landX + dx[i]
            ny = landY + dy[i]
            if 0 <= nx < size and 0 <= ny < size and graph[ny][nx] == 0:
                graph[ny][nx] = graph[landY][landX] + 1 # 방문체크
                queue.append((nx, ny))
    
    
testNum = int(input())

for _ in range (testNum):
    size = int(input())
    start = list(map(int, sys.stdin.readline().strip().split()))
    end = list(map(int, sys.stdin.readline().strip().split()))
    
    graph = [[0] * size for _ in range(size)]
    
    bfs(graph, start, end)
