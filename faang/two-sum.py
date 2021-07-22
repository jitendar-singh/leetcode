class Solution:
    def __init__(self,a: list,sum: int):
        self.a = a
        self.sum = sum
    
    def twosum(self)-> list:
        result = []
        for num in self.a:
            target = self.sum - num
            if target in self.a:
                num1 = self.a.index(num)
                num2 = self.a.index(target)
                result.append((num1,num2))
        return result
            # else:
            #     continue

a = [1,2,4,5,6,7,8]
ss = Solution(a,9)

output = ss.twosum()
print(output)
        
        