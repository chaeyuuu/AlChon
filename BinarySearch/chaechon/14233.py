import sys

input = sys.stdin.readline
n = int(input())
deadline = list(map(int, input().split()))
deadline.sort()

start, end = 1, deadline[-1]

while start <= end:
    mid = (start + end) // 2
    valid = True
    
    # 이 mid 값으로 모든 일의 마감기한이 가능한지 확인
    for i in range(n):
        if mid * (i+1) > deadline[i]:
            valid = False
            break
        
    # 가능하면 start = mid + 1 해서 확인
    # 불가능하면 end = mid - 1 해서 확인
    
    if valid == True:
        start = mid + 1
    else:
        end = mid - 1
            
print(end)