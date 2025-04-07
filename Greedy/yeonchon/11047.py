import sys
reader = sys.stdin.readline

n, k = map(int, reader().strip().split())

coinList = [int(reader().strip()) for _ in range(n)]
    
coinList.sort(reverse=True)
count = 0

for coin in coinList: 
    if k == 0:
        break
    if k >= coin:
        count += k // coin
        k %= coin
        
print(count)