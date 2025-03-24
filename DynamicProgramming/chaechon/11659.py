import sys

input = sys.stdin.readline

N, M = map(int,input().split())
print(N, M)

num_list = list(map(int, input().split()))
print(num_list)

for _ in range(M):
    # print_list.append((int, input().split()))
    i, j = (map(int, input().split()))
    print(i, j)
    
    result = 0

    for num in range(i-1, j):
        result += num_list[num]
    
    print(result)