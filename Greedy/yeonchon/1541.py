# 3 + 4 - 3 - 10 + 24 
# (3 + 4) - (3) - (10 + 24) = -30 
# - 사이사이에 있는 +들을 더 더해서 크기를 키우고 -로 부호를 만들어줌
# - 로 split 하고 사이사이를 다 더해서 빼줌

import sys
reader = sys.stdin.readline

input = reader().strip().split("-")

result = 0

# 첫 - 앞 쪽 모두 더하기
for exp in input[:1]:
    result += sum(map(int, exp.split("+"))) # sum함수: iterable요소를 모두 더해줌
    
# - 로 자른 부분식 더해서 -로 묶어서 빼기
for exp in input[1:]:
    result -= sum(map(int, exp.split("+")))
        
print(result)