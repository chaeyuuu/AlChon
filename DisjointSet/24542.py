import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x]) # 경로 압축
    return parent[x]

def union(x, y):
    parentX = find(x)
    parentY = find(y)
    
    if parentX == parentY:
        return
    if size[parentX] > size[parentY]:
        parent[parentY] = parentX
        size[parentX] += size[parentY]
    else:
        parent[parentX] = parentY
        size[parentY] += size[parentX]        
    
n, m = map(int, input().strip().split())

parent = [i for i in range(n+1)] # 자기 자신을 parent node
size = [1] * (n+1)

for _ in range(m):
    x, y = map(int, input().strip().split())
    union(x, y)
    
sum = 1
parentSet = set()
for i in parent:
    if i != 0: 
        parentSet.add(i)
        
for i in parentSet:
    sum *= size[i]
        
print(sum % 1000000007)    