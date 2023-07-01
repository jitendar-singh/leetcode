def finder(arr1, arr2):
    for item in arr1:
        if item not in arr2:
            return item

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,5]
print(finder(arr1,arr2))
