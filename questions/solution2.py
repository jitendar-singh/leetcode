class Solution:
    def longestsubstring(self,s: str)->int:
        left, right, n, ans, m = 0,0,len(s),0,{}

        while(left < n and right < n):
            element = s[right]
            if element in m:
                left = max(left,m[element]+1)
            m[element]= right
            ans = max(ans,right-left+1)
            right+=1
        return ans

ss = Solution()
print(ss.longestsubstring('bcdefghijklmnopqrstuvwxyzbcbb'))
print(ss.longestsubstring('babcsa'))