# Determine if a given array is sorted
def is_sorted_array(arr):
    
    if len(arr) < 2:
        return True
    
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

arr = [1,2,4,6,7,8,9,8]
print(is_sorted_array(arr))
# is_sorted_array(arr)
