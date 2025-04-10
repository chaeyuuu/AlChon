import sys
reader = sys.stdin.readline

n, k = map(int, reader().strip().split())

coinList = [int(reader().strip()) for _ in range(n)]
    
count = 0

for i in range(n-1, -1, -1): # 역순순회: n-1부터 0까지 -1 step으로 순회
    if k == 0:
        break
    if k >= coinList[i]:
        count += k // coinList[i]
        k %= coinList[i]
        
print(count)