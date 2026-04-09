
def seq_search(list, item):
    idx = 0
    while idx < len(list):
        if list[idx] == item:
            return idx
        idx += 1
    return None


nos = [3,1,4,2,5]
print(seq_search(nos, 2)) # expected output : 3
print(seq_search(nos, 4)) # expected output : 2

