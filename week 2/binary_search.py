def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None
    
    
nos = [1,3,5,7,9] # nos 'should' be ordered (sorted for binary search to work)
print(binary_search(nos, 5)) # expected output : 2
print(binary_search(nos, 11)) # expected output : None (indicating non-existent item)