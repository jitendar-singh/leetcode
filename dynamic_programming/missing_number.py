def find_missing_number(arr):
    n = len(arr)  # Number of elements in the original sequence
    expected_sum = (n * (n + 1)) // 2  # Expected sum of the sequence
    actual_sum = sum(arr)  # Sum of the given array
    missing_number = expected_sum - actual_sum
    return missing_number

print(find_missing_number([0,1,2,3,5,6,7,8,9]))
