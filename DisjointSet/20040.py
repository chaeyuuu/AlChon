import sys
input = sys.stdin.readline

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
    parent[parentX] = parentY
    return True

n, m = map(int, input().strip().split())
parent = [i for i in range(n)]

def cycle_check():
    for num in range(m):
        x, y = map(int, input().strip().split())
    
        if not union(x, y):
            return num+1
    return 0

print(cycle_check())