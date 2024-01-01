class Solution:
    def boats(self, peoples, limit):
        count = 0
        peoples.sort()
        l = 0
        h = len(peoples) - 1
        while(l<=h):
            if peoples[l] + peoples[h] <= limit:
                count+=1
                l+=1
                h-=1
            else:
                count+=1
                h-=1
        return count


s = Solution()
peoples = [1,2,3,2,1,3,2]
limit = 3
count = s.boats(peoples, limit)
print(count)