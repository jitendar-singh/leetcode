from collections import Counter
class Solution:
    def __init__(self) -> None:
        self.palindrome = {}
        self.loopflag = 0
    def longestPalindrome(self, s: str) -> str:
        end = len(s)
        i = 0
        new_str = ""
        res = ""
        while(i < end):
            for ch in range(end):
                new_str = new_str+s[ch]
                print(new_str)
            flag = self.checkPalindrome(new_str)
            if flag:
                self.store(new_str)
            i+=1
            if i >= end:
                self.loopflag+=1
                i = self.loopflag
                ch = i
            new_str=""
        for substr in self.palindrome.keys():
            max = 1
            if self.palindrome[substr] >= max:
                res = substr
                max = self.palindrome[substr]
        return res

        
    def checkPalindrome(self, new_str: str) -> bool:
        if new_str == new_str[::-1]:
            return True
        else:
            return False

    def store(self, new_str: str)-> dict:
        lenght = len(new_str)
        self.palindrome[new_str] = lenght
        # print(self.palindrome)
            

ss = Solution()
output = ss.longestPalindrome("cbbd")
# print(output)
