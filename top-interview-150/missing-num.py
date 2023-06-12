# Given an array of integers from 1 to n, where one number is missing, 
# write a Python function to find the missing number.

def find_missing_number(nums):
    n = len(nums)+1
    expected_sum = (n * (n+1))//2
    # print(expected_sum)
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number

numbers = [1, 2, 4, 6, 3, 7, 8]
missing_number = find_missing_number(numbers)
print("The missing number is:", missing_number)
