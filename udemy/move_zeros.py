class Solution:
    def move(self, nums):
        zero_index = 0
        for non_zero_index in range(0,len(nums)):
            if nums[non_zero_index] != 0:
                nums[zero_index] = nums[non_zero_index]
                zero_index+=1
        
        for i in range(zero_index,len(nums)):
            nums[i] = 0
        
        print(nums)

s = Solution()
s.move([0,1,0,0,3,0,5,6,0,0,7])

