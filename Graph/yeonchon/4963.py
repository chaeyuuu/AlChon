# 1은 땅 0은 바다
# bfs: 가로 세로 대각선으로 인접한 곳이 1인지 확인
# 리스트 안에 리스트 구조
# 해당 행에서 1인거만 저장
# 가장 먼저 나온 땅 start 로 넘김
# 가로세로대각선 인접 위치 계산 -> 그 위치가 1이면 queue에  -> 이미 본 위치 0으로 변화

import sys
from collections import deque

def bfs(graph, x, y):
    # 인접 위치 index
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    # 그래프의 인덱스를 접근할때는 x, y 순서 바꿔서
    graph[y][x] = 0 # 방문처리
    queue = deque([(x, y)])
    
    while queue:
        landX, landY = queue.popleft()
        for i in range(8):
            nx = landX + dx[i]
            ny = landY + dy[i]
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                graph[ny][nx] = 0 
                queue.append((nx, ny))


while True:
    # w = 너비 = 열, h = 높이 = 행
    w, h = map(int, sys.stdin.readline().strip().split())
    
    if w == 0 and h == 0:
        break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))
    
    count = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                bfs(graph, j, i)
                
    print(count)
    count = 0
                