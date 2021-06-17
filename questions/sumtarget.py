# # from typing import List


# # class Solution:
# #     def sumTarget(self,arr: List[int],target: int) -> List[int]:
# #         indexs = [i for i,value1 in enumerate(arr) for j,value2 in enumerate(arr) if value1+value2==target]
# #         return indexs

# # s= Solution()
# # a = [1,2,2,3]
# # answer = s.sumTarget(a,4)
# # print(answer)
# import collections

# a = [3,2,3]
# b = collections.Counter(a)
# majority = len(a)//2
# print(b)
# print(majority)
# for key, value in b.items():
#     if value > majority:
#         max = key
# print(max)

import collections
from typing import Collection


strs = ["eat","tea","tan","ate","nat","bat"]
l = []
for i in range(0,len(strs)):
    new = []
    for j in range(1,len(strs)):
        if(sorted(strs[i])==sorted(strs[j])):
            new.append(strs[j])
            strs.remove(strs[j])
        else:
            new.append(strs[i])
    l.append(new)
print(l)
# for x in range(0,len(l)):
#     for j in range(1,len(l)):
#         if(sorted(l[x])==sorted(l[j])):
#             l.remove(l[j])
# print(l)

    





                    
