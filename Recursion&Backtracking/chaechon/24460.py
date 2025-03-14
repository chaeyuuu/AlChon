import sys

input = sys.stdin.readline

n = int(input())
chairs = []

for _ in range(n):
    chairs.append(list(map(int, input().split())) )
    
def backtracking(n,x,y):
    if n == 1:
        return chairs[x][y] # 1개로 나눠질 때 위치 반환
    
    else:
        news = []
        
        news.append(backtracking(n//2, x, y)) # 2사분면
        news.append(backtracking(n//2, x+n//2, y)) # 3사분면
        news.append(backtracking(n//2, x, y+n//2)) # 1사분면
        news.append(backtracking(n//2, x+n//2, y+n//2)) # 4사분면

        news.sort()
        return news[1]

print(backtracking(n,0,0))