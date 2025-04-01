# 미로 탐색

import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int,input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip()))) # 레전드 똥교소 \n 까지 입력되어서 strip() 해줘야했음

def bfs(x,y):
    
    count = 1
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
        
    queue = deque()
    queue.append((x,y))
    
    while queue:
        a,b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
        
            if 0<=nx<N and 0<=ny<M:
                if maze[nx][ny] == 1:
                    queue.append((nx,ny))
                    maze[nx][ny] = maze[a][b] + 1
                    
    return maze[N-1][M-1]
    
print(bfs(0,0))
