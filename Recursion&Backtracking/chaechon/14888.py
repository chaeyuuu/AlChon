import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split())) # append 사용하면 이중 리스트가 됨
op_list = list(map(int, input().split()))
result_list = []
max_result , min_result = -1e9, 1e9
ops = []
symbol = ['+', '-', '*', '/']

for i in range(4):
    ops.extend(op_list[i] * symbol[i])
    
possilbe_list = set(permutations(ops, len(ops))) # set 사용해서 중복 제거

for op in possilbe_list:
    temp = num_list[0]
    for i in range(len(ops)):
        if op[i] == '+':
            temp += num_list[i+1]
        elif op[i] == '-':
            temp -= num_list[i+1]
        elif op[i] == '*':
            temp *= num_list[i+1]
        elif op[i] == '/':
            if temp < 0:
                temp = -(-temp // num_list[i+1])
            else:
                temp = temp // num_list[i+1]

    max_result = max(max_result, temp)
    min_result = min(min_result, temp)

print(max_result)
print(min_result)


