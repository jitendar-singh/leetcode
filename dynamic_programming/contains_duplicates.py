def contains_duplicates(arr):
    
    # return len(arr) != len(set(arr))
    
    index = {}
    for item in arr:
        if item not in index:
            index[item]=1
        else:
            return True
    return False
arr = [1,2,3,4,5,-1]
print(contains_duplicates(arr))
