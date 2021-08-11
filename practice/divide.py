class Solution:
    def divide(self, dividend: float, divisor: int) -> float:
        output = dividend
        counter = 0
        while output:
            # if divisor > 0:
            output = output - divisor
            counter+=1
            if output < 1:
                counter+=output
                print(output)
                break
            # else:
            #     output = output + divisor
            #     counter+=1
        return counter

s = Solution()
res = s.divide(18,2)
print(res)