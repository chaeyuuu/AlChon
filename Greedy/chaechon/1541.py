# 잃어버린 괄호

import sys
input = sys.stdin.readline

string = input().split('-')
count = []

for i in string:
    temp = 0
    for j in i.split('+'):
        temp += int(j)
    count.append(temp)

result = count[0]

for i in count[1:]:
    result -= i
print(result)