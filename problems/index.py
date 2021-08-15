def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while(left<=right):
        middle = (left+right)//2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle-1
        else:
            left = middle+1
    return -1


arr = [1,2,3,4,5,6]
target = 6

result = binarySearch(arr, target) #index: 5

if result != -1:
    print("Element is present at index %d"%result)
else:
    print("Element not found")
