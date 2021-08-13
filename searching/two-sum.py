class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        i = 0
        for i in range(len(nums)-1):
            req = target - nums[i]
            if req in range((i+1),len(nums)-1):
                output.append(i)
                output.append(nums.index(req))
                return output
s = Solution()
nums = list[int]
nums = [3,2,4]
res = s.twoSum(nums,6)
print(res)