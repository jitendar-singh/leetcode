
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0
        print(nums)

arr = [0,2,0,4,0,56,89,0,0,0]
s = Solution()
s.moveZeroes(arr)
