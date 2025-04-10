import sys
reader = sys.stdin.readline

input = reader().strip().split("-")

result = 0

# 첫 - 앞 쪽 모두 더하기
for exp in input[:1]:
    result += sum(map(int, exp.split("+"))) # sum함수: iterable요소를 모두 더해줌
    
# 첫 - 뒤 쪽 모두 계산
for exp in input[1:]:
    result -= sum(map(int, exp.split("+"))) # -로 시작하는 거는 빼는게 아니라 -40을 더한다고 생각
        
print(result)