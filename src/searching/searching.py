def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr) - 1)
    while end >= start:
        mid_index = (start + end) // 2
        if arr[mid_index] == target:
            return mid_index
        else:
            if arr[mid_index] > target:
                end = mid_index - 1
            if arr[mid_index] < target:
                start = mid_index + 1 



    return -1  # not found
