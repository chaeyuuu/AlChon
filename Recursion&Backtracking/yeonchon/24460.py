def recursion(input_list, lineNum):
    if lineNum == 2:
        flat_list = [j for i in input_list for j in i]
        flat_list.sort()
        return flat_list[1]
    
    n = lineNum//2
    
    searchList1 = [i[:n] for i in input_list[:n]]
    searchList2 = [i[n:] for i in input_list[:n]]
    searchList3 = [i[:n] for i in input_list[n:]]
    searchList4 = [i[n:] for i in input_list[n:]]

    findList = []
    findList.append(recursion(searchList1, n))
    findList.append(recursion(searchList2, n))
    findList.append(recursion(searchList3, n))
    findList.append(recursion(searchList4, n))
    
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

print(recursion(input_list, lineNum))