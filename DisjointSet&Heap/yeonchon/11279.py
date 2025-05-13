# 0번 인덱스는 사용 X
# 왼쪽 자식 노드의 인덱스 = 부모 노드의 인덱스 * 2 
# 오른쪽 자식 노드의 인덱스 = 부모 노드의 인덱스 * 2 + 1
# 부모 노드의 인덱스 = 자식 노드의 인덱스 / 2

import sys
import heapq
input = sys.stdin.readline
    

num = int(input().strip())
maxHeap = []

for _ in range(num):
    x = int(input().strip())
    
    if x == 0:
        if len(maxHeap) == 0:
            print(0)
        else:
            print(-heapq.heappop(maxHeap))
            
    else:
        heapq.heappush(maxHeap, -x)
            
        