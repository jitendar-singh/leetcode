from typing import List
class Solution:
    def savePeople(self,people: List[int],limit: int) -> int:
        left = 0
        right = len(people)-1
        boats = 0
        people.sort()
        while(left<=right):
            if left == right:
                boats+=1
                break
            elif people[left] + people[right]<=limit:
                boats+=1
                left+=1
                right-=1
            else:
                right-=1
                boats+=1
        return boats

s= Solution()
arr = [3,5,3,4]
limit = 5
print(s.savePeople(arr,limit))

