indent = "  "
invocation_count=0

def merge_sort(arr):
    print(" ")
    global indent, invocation_count
    indent += "  "
    invocation_count += 1
    
    print(f"{indent} [merge_sort({invocation_count})] arr =", arr)
    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    
    print(f"{indent} [merge_sort({invocation_count})] arr[:{mid}] = {arr[:mid]}, arr[{mid}:] = {arr[mid:]}")
    
    left = merge_sort(arr[:mid])
    print(f"{indent} [merge_sort({invocation_count})] left =", left)
    
    right = merge_sort(arr[mid:])
    print(f"{indent} [merge_sort({invocation_count})] right =", right)

    merge_sort_result = merge(left, right)
    print(f"{indent} [merge_sort({invocation_count})] merge_sort_result = {merge_sort_result}")
    
    return merge_sort_result

def merge(left, right):
    result = []
    i = j = 0
    print(f"{indent} [merge({invocation_count})] left={left}, right={right}")
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    print(f"{indent} [merge({invocation_count})] result={result}")
    return result

arr = [38, 27, 43, 3, 9]
print(merge_sort(arr))