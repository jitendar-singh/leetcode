# Given an array of integers, a value Sum , determine if there is a subset of the given set with sum equal to given sum

def has_subset(arr, target_sum):
    target = {}
    l = set()
    for item in arr:
        if item not in target:
            if item < target:
                target[target_sum] = l.add(item)


arr = [3,34,4,12,5,2]
N = 6
target_sum = 9
