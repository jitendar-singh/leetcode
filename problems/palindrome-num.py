class Solution:
    def ispalindrome(self,num: int) -> bool:
        x = num
        rem = 0
        while(num > 0):
            rem = (rem*10) + num % 10 #1 12 12 1 121 
            num//=10
        print(rem)
        if rem == x:
            return True
        else:
            return False

s = Solution()
is_palindrome = s.ispalindrome(121)
print(is_palindrome)




# a = 0
# rev = 0
# a = 121
# while a > 0:
#     rev = (rev*10)+(a%10)
#     a//=10
# print(rev)
