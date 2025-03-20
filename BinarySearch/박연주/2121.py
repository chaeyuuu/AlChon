import sys

def findRactangle(size_x, size_y):
    count = 0
    
    for i in pointSet:
        x = i[0]
        y = i[1]
        
        if (x + size_x, y) in pointSet and (x, y + size_y) in pointSet and (x + size_x, y + size_y) in pointSet:
            count+=1
            
    return count

pointNum = int(sys.stdin.readline().strip())
rectangle = list(map(int, sys.stdin.readline().strip().split()))

pointSet = set()
for i in range(pointNum):
    pointSet.add(tuple(map(int, sys.stdin.readline().strip().split())))

print(findRactangle(rectangle[0], rectangle[1]))