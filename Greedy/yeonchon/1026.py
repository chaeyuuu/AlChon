import sys
reader = sys.stdin.readline

n = int(reader().strip())
listA = list(map(int, reader().strip().split()))
listB = list(map(int, reader().strip().split()))

listA.sort()
listB.sort(reverse=True)

sum = 0
for i in range(n):
        sum += listA[i] * listB[i]
        
print(sum)