import math
n = int(input())

q = int(math.sqrt(n)) # ceil 함수 쓰면 틀림 why?

if q * q >= n:
    print(q)
else :
    print(q + 1)