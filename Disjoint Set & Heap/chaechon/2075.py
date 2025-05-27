import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    row = list(map(int, input().split()))
    for num in row:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            # 인덱스 0에 가장 작은 원소가 저장 되어있음
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
                

print(heap[0])