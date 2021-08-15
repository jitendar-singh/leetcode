# A = [-14, -10, 2, 108, 108, 108, 243, 285, 285, 285,401]
# target = 108
# output = 3 index 3 is the first occurance of 108

def find(A: list[int],key: int) -> int:
    low = 0
    high = len(A)-1

    while(low <= high):
        mid = (low + high) // 2

        if(A[mid] > key):
            high = mid - 1
        elif(A[mid] < key):
            low = mid + 1
        else:
            if mid - 1 < 0:
                return mid
            if(A[mid-1]!= key):
                return mid
            high = mid - 1
    return None

A = [-14, -10, 2, 108, 108, 108, 243, 285, 285, 285,401]
key = 285
res = find(A,key=key)
print(res)