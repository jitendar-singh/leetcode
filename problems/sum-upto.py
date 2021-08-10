class Solution:
    def add_it_up(self,limit: int)-> int:
        result = 0
        if limit <= 0:
            return 0
        else:
            i = 1
            for i in range(limit+1):
                result +=i
        return result
            

s = Solution()
num = 4
sum = s.add_it_up(num)
print(sum)