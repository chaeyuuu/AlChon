import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            temp = heapq.heappop(heap)[1]
            print(temp)
    else:
        # heap은 기본적으로 최소힙
        heapq.heappush(heap, (-x,x))