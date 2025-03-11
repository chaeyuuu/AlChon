def recursion(input_list, lineNum, x, y):
    if lineNum == 2:
        flat_list = [input_list[x][y], input_list[x][y + 1], input_list[x + 1][y], input_list[x + 1][y + 1]]
        flat_list.sort()
        return flat_list[1]
    
    n = lineNum // 2

    findList = []
    findList.append(recursion(input_list, n, x, y))
    findList.append(recursion(input_list, n, x + n, y))
    findList.append(recursion(input_list, n, x, y + n))
    findList.append(recursion(input_list, n, x + n, y + n))
    
    findList.sort()
    return findList[1]

lineNum = int(input())
input_list = []

if lineNum == 1:
    print(input())
    exit(0)
else:
    for i in range(lineNum):
        line = [int(j) for j in input().split()]
        input_list.append(line)

print(recursion(input_list, lineNum, 0, 0))