class Solution:
    def substr(self, s):
        left, right, answer = 0, 0, 0
        m = {}
        
        for i in range(len(s)):
            if s[i] in m:
                left = max(left, m[s[i]]+1)
            right+=1
            m[s[i]] = i
            answer = max(right - left, answer)
        return answer


sent = "abcadcefgd"
ss = Solution()
output = ss.substr(sent)
print(output)