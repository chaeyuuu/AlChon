# 섬의 개수

# 문제
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x,y):

    dx = [0,0,-1,1,1,-1,-1,1] # 상하좌우대각선
    dy = [-1,1,0,0,-1,-1,1,1]
    
    visited[x][y] = 1 # 방문으로 바꾸기

    queue = deque()
    queue.append((x,y))
    
    while queue:
        a,b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<= nx <h and 0<=ny < w: # 범위 체크
                if visited[nx][ny] == 0 and landmap[nx][ny] == 1: # 근처에 땅이 있는데 방문 안 했으면 
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
            
            
while True:
    w,h = map(int, input().split())
    if w==0 and h==0:
        break
    
    count = 0
    landmap = [] # 지도 배열
    visited = [[0] * w for _ in range(h)] # 방문 기록 저장 

    for _ in range(h):
        landmap.append(list(map(int, input().split())))
    # print(landmap)
    
    for i in range(h):
        for j in range(w):
            if landmap[i][j] == 1 and visited[i][j] == 0: # 땅이고 방문하지 않았다면  
                bfs(i,j) # 주변 탐색 
                # print(visited)
                count+=1
    
    print(count)
