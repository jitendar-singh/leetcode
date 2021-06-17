from typing import List


class Solution:
    def slidingwindow(self,arr: List[int],winsize: int)->int:
        i = 0
        ma = 0
        add = 0
        y = 0
        while(len(arr)-i > winsize-1):
            start = i
            y = 0
            add = 0
            while(y<winsize):
                # print(start)
                add+=arr[start]
                if(add > ma):
                    ma = add
                start+=1
                y+=1
            i+=1
        return ma

s = Solution()
a = [1, 2, 100, -1, 5]
n = 3
result = s.slidingwindow(a,n)
print(result)




