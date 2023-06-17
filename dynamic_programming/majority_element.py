# Given an array of integers find if it has any majority elements
# [1,2,3,1,1], n = 5 , majority > n/2 

def majority_elements(arr):
    count, majority_items = {}, []
    n = len(arr)//2
    for item in arr:
        if item not in count:
            count[item] = 1
        else:
            count[item]+=1
            if count[item] > n:
                majority_items.append([item,count[item]])
    if majority_items is not None:
        return majority_items
    else:
        return None

arr = [1,2,1,1,3]
print(majority_elements(arr))

