class Solution:

    def threesum(self, a: list)-> list[list[int]]:
        length = len(a)
        output = [()]
        a.sort()
        print(a)
        left = 1
        right = length - 1
        for i in range(length-2):
            print(a[i], a[left], a[right])
            if a[i]+a[left]+a[right] == 0:
                if a[i] != a[right] and a[left]!= a[right] and a[i]!= a[left]:
                    output.append([a[i],a[left],a[right]])
                    print(output)
                    left+=1
                    right-=1
            elif a[i] == a[left]:
                left+=1
            elif a[i] == a[right]:
                right-=1
            elif a[left] == a[right]:
                left+=1
        return output

s = Solution()
aa = [-1,0,1,2,-1,4]
result = s.threesum(aa)
print(result)
            


        