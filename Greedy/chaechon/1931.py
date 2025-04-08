# 회의실 배정

import sys 
from collections import deque

input = sys.stdin.readline
N = int(input())
meetings=[]
count = 0 
next = 0

for _ in range(N):
    a, b = map(int, input().split())
    meetings.append((a,b))

meetings.sort(key=lambda x: (x[1], x[0]))
# print(meetings)

for a, b in meetings:
    # print(a,b)
    if a>=next:
        # 회의 끝나는 시간보다 시작시간이 크면 시작 가능 -> 그 회의시간의 끝나는 시간을 다음 시작 가능한 시간으로 집어넣기
        count +=1
        next = b

print(count)
