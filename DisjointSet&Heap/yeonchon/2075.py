import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
heap = list()
for i in range(n):
    
    if len(heap) == 0:
        heap = list(map(int, input().strip().split()))
        heapq.heapify(heap)
    else:
        for num in map(int, input().strip().split()):
            if heap[0] < num:
                heapq.heappushpop(heap, num) # 가장 min 값을 빼고 넣음
                
print(heap[0])