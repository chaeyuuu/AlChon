import sys
sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parentX = find(x)
    parentY = find(y)
    
    if parentX == parentY:
        return False
    
    if rank[parentX] > rank[parentY]:
        parent[parentY] = parentX # 높이가 작은 쪽을 큰 쪽에 붙임
    elif rank[parentX] < rank[parentY]:
        parent[parentX] = parentY
    else:
        parent[parentX] = parentY
        rank[parentX] += 1
    return True

n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

def solve():
    for num in range(m):
        x, y = map(int, input().split())
        if not union(x, y):
            print(num + 1)
            return
    print(0)

solve()