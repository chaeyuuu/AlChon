# 나이트의 이동
import sys
from collections import deque

input = sys.stdin.readline

def bfs(n,m):
    
    dx = [2,1,-1,-2,-2,-1,1,2]
    dy = [-1,-2,-2,-1,1,2,2,1]
    
    queue = deque()
    queue.append((n,m))
    
    visited[n][m] = 1
    
    while queue:
        
        a,b = queue.popleft()
        
        if a == dest_x and b == dest_y:
            return 0
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<size and 0<=ny<size:
                 
                if nx == dest_x and ny == dest_y:
                    visited[nx][ny] = 1
                    return chess[a][b] + 1
                
                elif visited[nx][ny] == 0:
                    chess[nx][ny] = chess[a][b] + 1
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    # print(chess)
        
        
        
T = int(input())

for _ in range(T):
    size = int(input())
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    
    chess = [[0]*size for _ in range(size)]
    visited = [[0]*size for _ in range(size)]
    # print(chess)
    print(bfs(start_x, start_y))
    
    
