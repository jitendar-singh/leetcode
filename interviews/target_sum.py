# Given a list of integers, write a Python function to find the two numbers that add up to a given target sum.

def target_sum(nums, target):
    for num in nums:
        if (target - num) in nums:
            return num, target-num

numbers = [2,9, 4, 7, 11, 15]
target = 11
result = target_sum(numbers,target)
print(result)