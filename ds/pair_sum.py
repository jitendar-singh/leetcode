def pair_sum(arr, target_sum):
    seen , output = set(), set()
    target = 0
    if len(arr) < 2:
        return False

    for item in arr:
        target = target_sum - item

        if target not in seen:
            seen.add(item)
        else:
            output.add((min(item,target),max(item,target)))
        # print(seen)
    return output
        
arr = [1,3,2,2]
target_sum = 4
print(pair_sum(arr, target_sum))