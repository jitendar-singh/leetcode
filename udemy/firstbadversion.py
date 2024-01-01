class Solution:
    def isBadVersion(self, version):
        return version >= 3
    
    def firstBadVersion(self, nums):
        left , right , mid = 1, len(nums), 0

        while left <= right:
            mid = left+(right-left)//2
            if not self.isBadVersion(nums[mid]):
                left = mid +1
            else:
                right = mid
        return left

s = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
print(s.firstBadVersion(nums))
    