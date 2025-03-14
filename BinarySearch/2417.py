def binarySearch(start, end):

    if(start > end):
        return start
    
    mid = (start + end) // 2
    target = mid ** 2
    
    if target == n:
        return mid
    elif target < n:
        return binarySearch(mid + 1, end)
    else:
        return binarySearch(start, mid - 1)
    
n = int(input())
start = 0
end = n

print(binarySearch(start, end))