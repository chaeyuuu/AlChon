import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):    
    queue = deque([(x, y)])
    graph[x][y] = 0
    num = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    num += 1
                    graph[nx][ny] = 0 # 중복 카운트 없게
    
    return num
    
n = int(input().strip())
count = 0
output = []
graph = []

for _ in range(n):
    graph.append([int(char) for char in input().strip()])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count += 1
            output.append(bfs(i, j))

sys.stdout.write(f"{count}\n")

output.sort()
for num in output:
    sys.stdout.write(f"{num}\n")

sys.stdout.flush()