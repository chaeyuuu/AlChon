# DP 없이 풀기
# def fibonacci(n):
#     if n <= 1
#         return n
#     if n >= 2:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# n = int(input())
# print(fibonacci(n))

########
# 2 -> 0, 1 호출 & 반환
# ...
# 7 -> 6, 5
# 8 -> 7, 6 호출
# 9 -> 8, 7 호출
# 10 -> 9, 8 호출

# 1 ~ 8 가 2번씩 호출됨 -> DP 는 이 값을 저장해놓음 = 효율
########
def fibonacci(n):
    if n <= 1:
        return n
    # 이미 값이 계산되어 있다면
    if n in fibo_dict.keys():
        return fibo_dict.get(n)
    # 값이 계산되어 있지 않으면 계산하여 저장
    fibo_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibo_dict[n]
    
n = int(input())
fibo_dict = dict()
print(fibonacci(n))
