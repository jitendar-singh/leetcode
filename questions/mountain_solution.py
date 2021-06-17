from typing import List
class Solution:
    # 1,2,3,4,5,3,2,1
    def getMountainSeq(self,arr: List[int])-> bool:
        if len(arr)<3:
            return False
        y = 1
        while(y < len(arr) and arr[y]>arr[y-1]):
            y+=1
        if(y ==1 or y == len(arr)):
            return False
        while(y < len(arr) and arr[y]<arr[y-1]):
            y+=1

        return y==len(arr)

s = Solution()
arr = [9,8,7,6,5,4,3,2,1,0]
print(s.getMountainSeq(arr))
# if(len(A)<3):
#             return False
        
#         i = 1
#         while(i<len(A) and A[i]>A[i-1]):
#             i+=1
        
#         if(i==1 or i==len(A)):
#             return False
        
#         while(i<len(A) and A[i]<A[i-1]):
#             i+=1
        
#         return i==len(A)