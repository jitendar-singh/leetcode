def find_fixed_point(A):
    left = 0
    right = len(A) - 1
    
# A = [-10, -5, 0, 3, 7]
    while(left <= right):
        mid = (left + right)//2
        # print(mid)
        if A[mid] < mid:
            left = mid+1
        elif A[mid] > mid:
            right = mid-1
        else:
            return A[mid]
    return None
A = [-10, -5, 0, 3, 7]
B = [0,2,5,8,17]
res = find_fixed_point(B)
print(res)