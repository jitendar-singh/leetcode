class Solution:
    #using List
    def floccurance(self, s, target):
        m = {}
        answer = []

        for i in  range(len(s)):
            if s[i] == target:
                answer.append(i)
                m[s[i]] = answer
        print(m)
        return answer[0], answer[-1]

    # using binary search technique
    def firstIndex(self, nums, target):
        left, right, mid = 0 , len(nums) - 1, 0


        while left <= right:
            mid = (left + right)//2
           
            if nums[mid] == target:
                # If mid is the first occurance
                if mid == 0 or nums[mid -1] !=target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def lastIndex(self, nums, target):
        left, right, mid = 0 , len(nums) - 1, 0


        while left <= right:
            mid = (left + right)//2
           
            if nums[mid] == target:
                # If mid is the lasr occurance
                if mid == len(nums)-1 or nums[mid + 1] !=target:
                    return mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
                
    def searchrange(self, nums, target):
        if not nums or target < nums[0]:
            return [-1, -1]
        
        f = self.firstIndex(nums, target)
        l = self.lastIndex(nums, target)
        return [f, l]


ss = Solution()
input = [10, 11,11,11,11,11,13,13,13, 15, 17, 18]
first, last = ss.searchrange(input, 100)
print(first,':', last)
