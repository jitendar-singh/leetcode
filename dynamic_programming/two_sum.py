def two_sum(arr, target):
    for item in arr:
        if target - item in arr:
            result = find_index(arr, [item, target-item])
            return result

def find_index(arr,items):
    result = []
    for item in items:
        result.append(arr.index(item))
    return result


arr = [3, 6, 12, 14]
target = 25
print(two_sum(arr,target))