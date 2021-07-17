'''
0 1 1 2 3 5 8 ... n
'''

class Solution:
    
    def fibonacci(self,n: int) -> list:
        i = 0
        j = 1

        # print(i)
        # print(j)
        while i <= n: #5
            temp = i+j # 1 2 3 5
            print(temp)
            i = j # 1 2 3 5
            j = temp # 1 1 2 3

# 0 1 1 2 3 5 
s = Solution()
s.fibonacci(5)


            

