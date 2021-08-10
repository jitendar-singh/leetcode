class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        have = str("")
        # words.reverse()
        for w in words:
            have = have+w
            if w not in s and have != s :
                return False
        return True
        
 
ss = Solution()
# s = str("iloveleetcode")
# words = ["i","love","leetcode","apples"]
result = ss.isPrefixString("iloveleetcode",["i","love","leetcode","apples"])
print(result)