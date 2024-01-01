def maximum_element(arr):
    max_element = arr[0]
    for i in arr[1:]:
        if i > max_element:
            max_element = i
    return max_element

arr = [1000,2,300,4,5,6,7,8,9,10000]
print(maximum_element(arr))