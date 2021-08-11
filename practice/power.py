class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        while n!=0:
            result*=x
            n-=1
        return result
s = Solution()
res = s.myPow(2.1,3)
print(res)
        
                