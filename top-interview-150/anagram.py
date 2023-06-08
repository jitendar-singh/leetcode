class Solution:

    def isAnagram(self,s1: str, s2: str)-> bool:
        s1 = s1.replace(" ","").lower()
        s2 = s2.replace(" ","").lower()

        return sorted(s1) == sorted(s2)
    

s = Solution()
res = s.isAnagram("cat si", "tac is")
print(res)