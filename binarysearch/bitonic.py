def bitonic_peak(A: list[int]) -> int:
    # A = [1, 6, 5, 4, 3, 2, 1]
    # output = 6
    low  = 0
    high = len(A) - 1
    # peak = 0
    while(low <= high):
        mid = (low+high) // 2
        if A[mid] > A[mid+1] and A[mid] > A[mid-1]:
            return A[mid]
        elif A[mid] < A[mid-1]:
            high = mid-1
        else:
            low = mid+1
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
res = bitonic_peak(A)
print(res)
    