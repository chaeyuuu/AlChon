import sys
import math

def checkWorkableTime(time):
    for i in range(len(deadline)):
        # 일하는 시간 * 몇번째 일인지가, 마감 기한을 넘어서면 안 됨
        if deadline[i] < (time * (i + 1)):
            return False
    return True
    
def binarySearch(low, high):
    max_value = -1
    
    while low <= high:
        mid = (high + low) // 2
         
        # 마감기한 안에 일이 가능하면, 최댓값을 구하기 위해 일 시간을 늘려본다.
        if checkWorkableTime(mid):
            max_value = mid
            low = mid + 1
        else: # 마감기한 안에 일이 불가능하면, 일 시간을 줄이면서 다시 테스트
            high = mid - 1  
            
    return max_value  
            
n = int(sys.stdin.readline().strip())
deadline = list(map(int, sys.stdin.readline().strip().split()))
deadline.sort()

low = 1 # 마감 기한의 최솟값은 1
high = deadline[0] # 첫 마감기한 통과를 위해, 일한 시간은 무조건 이 이하가 되어야함.

print(binarySearch(low, high))