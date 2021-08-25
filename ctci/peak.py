class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        target,num,output = 0, 0, 0
        for num in range(len(nums)):
            if nums[num] > target:
                # output = num
                target = nums[num]
        return nums.index(target)
s = Solution()
nums = [1,2,7,89,9,90]
output = s.findPeakElement(nums)
print(output)