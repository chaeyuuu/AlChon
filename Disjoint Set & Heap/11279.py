import sys
input = sys.stdin.readline

N = int(input())
list = []

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if len(list) == 0:
            print(0)
        else:
            temp = list[-1]
            print(list[-1])
            list.pop()
    else:
        list.append(x)
        list.sort()