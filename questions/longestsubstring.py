class Solution:
    def lenghtofLongestSubstring(self,s: str)-> int:
        left, right, ans, m, n  = 0,0,0,{},len(s)
        while(left < n and right < n):
            el = s[right]
            if(el in m):
                left = max(left,m[el]+1)
            m[el] = right
            ans = max(ans,right-left+1)
            right+=1
        return ans  

ss = Solution()
print(ss.lenghtofLongestSubstring('bcdefghijklmnopqrstuvwxyzbcbb'))
print(ss.lenghtofLongestSubstring('babcsa'))
