# 앞에 회의 endTime 보다 시작시간이 같거나 큰것 중에, 
# 끝나는 시간이 가장 짧은거
# + 이에 적합한 회의가 여러개 있다면!!! 시작시간이 가장 이른 회의를 선택

import sys
reader = sys.stdin.readline

num = int(reader().strip())

confList = []
for i in range(num):
    confList.append(tuple(map(int, reader().strip().split())))

count = 0
endTime = 0

# 끝나는 시간을 기준으로 sorting
# x[1]으로 정렬 중 동일한 값이 있다면 x[0]으로 정렬
confList.sort(key=lambda x: (x[1], x[0]))

for conf in confList:
    # 시작시간이 앞 회의 끝나는 시간과 같거나 이후인가
    if endTime <= conf[0]:
        print(conf)
        count += 1
        endTime = conf[1]
        
print(count)