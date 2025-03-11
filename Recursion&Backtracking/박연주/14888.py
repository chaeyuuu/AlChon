def dfs(depth, result, add, sub, mul, div):
    global max_value, min_value
    
    # 최대 최소 저장하고 리턴
    if depth == list_size:
        max_value = max(result, max_value)
        min_value = min(result, min_value)
        return
    
    if add:
        dfs(depth+1, result+input_list[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth+1, result-input_list[depth], add, sub-1 , mul, div)
    if mul:
        dfs(depth+1, result*input_list[depth], add, sub, mul-1, div)
    if div:
        dfs(depth+1, int(result/input_list[depth]), add, sub, mul, div-1)
    
        
    
list_size = int(input())
input_list = [int(i) for i in input().split()]
operator_list = [int(i) for i in input().split()]

max_value = -1e9
min_value = 1e9

dfs(1, input_list[0], operator_list[0], operator_list[1], operator_list[2], operator_list[3])

print(max_value)
print(min_value)