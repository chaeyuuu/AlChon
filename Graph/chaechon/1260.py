# DFS와 BFS
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.


# dfs는 스택, bfs는 큐 자료구조 이용

import sys

input = sys.stdin.readline
N,M,V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)] # 정점 저장 스택
visited_dfs = [0] * (N+1) # 방문 여부 저장 
visited_bfs = [0] * (N+1) # 방문 여부 저장 

for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1 # 연결된 노드들 1로 표시
    
def dfs(V):
    visited_dfs[V] = 1 # 방문처리
    print(V, end=' ') # 출력
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited_dfs[i] == 0: # 연결되어있지만 방문 안 한 애들
            dfs(i)
            
def bfs(V):
    queue = [V]
    visited_bfs[V] = 1
    while queue: # 큐가 빌 때까지 반복
        V = queue.pop(0) # 맨 처음에 있는 애 제거 및 V에 저장
        print(V, end=' ')
        for i in range(1, N+1):
            if graph[V][i] == 1 and visited_bfs[i] == 0: # 연결되어있지만 방문 안 한 애들
                queue.append(i) # 큐 뒤쪽에 추가
                visited_bfs[i] = 1 # 방문했다고 표시
    
dfs(V)
print()
bfs(V)