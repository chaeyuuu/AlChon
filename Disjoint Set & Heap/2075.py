import sys

input = sys.stdin.readline

N = int(input())
duu = []
for _ in range(N):
    x = list(map(int, input().split()))
    duu.append(x)

duu_1 = sum(duu,[])    
duu_1.sort(reverse=True)
print(duu_1[N-1])