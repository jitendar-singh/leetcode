# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

class Solution:
    def parser(self, s: str) -> str:
        return s.replace('()','o').replace('(al)','al')

ss = Solution()
cmd = 'G()(al)'
output = ss.parser(cmd)
print(output)
