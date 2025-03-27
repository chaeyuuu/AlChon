def numberListSum():
    temp = 0
    for i in numberList:
        temp += i
        sum.append(temp)

def sumRange(i, j):
    if i == j:
        return numberList[i - 1]
    return sum[j] - sum[i - 1] # (1~j 까지의 합) - (1~i-1 까지의 합) = i~j까지의 합
        
import sys

num, sumNum = map(int, sys.stdin.readline().strip().split())
numberList = list(map(int, sys.stdin.readline().strip().split()))
sum = [0] # 입력 범위 조정: 0번째 인덱스 초기화

numberListSum()

for k in range(sumNum):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(sumRange(i, j))
    