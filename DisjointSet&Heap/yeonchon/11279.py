# 0번 인덱스는 사용 X
# 왼쪽 자식 노드의 인덱스 = 부모 노드의 인덱스 * 2 
# 오른쪽 자식 노드의 인덱스 = 부모 노드의 인덱스 * 2 + 1
# 부모 노드의 인덱스 = 자식 노드의 인덱스 / 2

import sys
input = sys.stdin.readline
    

num = int(input().strip())
priorityQueue = [0] * (num+ 1 )# 0번 인덱스는 사용 X
size = 0 

for i in range(num):
    x = int(input().strip())
    if x == 0:
        if size == 0:
            print(0)
        else:
            print(priorityQueue.pop(1))
            
            size -= 1
            index = 1
            lastNode = priorityQueue.pop(size)
            priorityQueue.insert(1, lastNode)
            
            # heapify (down-heap)
            while index <= size:
                left = index*2
                right = index*2 + 1
                
                # 자식 노드가 없을때
                if left > size: 
                    break
                
                # 왼쪽 자식 노드만 있을때
                elif left == size: 
                    if priorityQueue[left] > lastNode:
                        priorityQueue[index] = priorityQueue[left]
                        priorityQueue[left] = lastNode
                        index = left
                    break
                
                # 두 자식 노드 다 있을 때
                else: # 두 자식 중 하나가 자신보다 클때, 더 큰 자식과 자리를 바꾼다.
                    if priorityQueue[left] > lastNode or priorityQueue[right] > lastNode:
                        if priorityQueue[left] > priorityQueue[right]: # 더 큰거랑 바꿔줌
                            priorityQueue[index] = priorityQueue[left]
                            priorityQueue[left] = lastNode
                            index = left
                        else:
                            priorityQueue[index] = priorityQueue[right]
                            priorityQueue[right] = lastNode
                            index = right
                    else: # 두 자식이 모두 나보다 작을때
                        break
                        
            
    else:
        size += 1
        index = size

        # heapify (up-heap)
        while index > 1 and x > priorityQueue[index//2]:
            priorityQueue[index] = priorityQueue[index//2] # 부모를 밑으로 내림
            index //= 2
        priorityQueue[index] = x
            
        