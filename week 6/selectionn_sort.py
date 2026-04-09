def selection_sort(arr):
    print("list=",arr)
    n = len(arr)

    for i in range(n):
        min_index = i

        # find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"[i={i}] min_index = ",min_index)

        # swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"[i={i}] arr =",arr)
    return arr


### Example usage


nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))

