def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Maximum subarray sum is: {max_subarray_sum(arr)}")
