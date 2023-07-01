# def find_largest_continuous_sum(arr):
#     max_sum = arr[0]
#     current_sum = arr[0]
    
#     for num in arr[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#         if current_sum < 0:
#             current_sum = 0
    
#     return max_sum
# arr = [-2, 3, -1, 5, 4]
# largest_sum = find_largest_continuous_sum(arr)
# print(largest_sum)  # Output: 11

def find_largest_continuous_sum(arr):
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(current_sum, max_sum)

        if current_sum < 0:
            current_sum = 0
    return max_sum


arr = [1,2,-1,3,4,10,10,-10,-1]
largest_sum = find_largest_continuous_sum(arr)
print(largest_sum)  # Output: 29