arr = [0,1,0,3,12,97,78,0,76]

for _, value in enumerate(arr):
    if value == 0:
        arr.append(value)
        arr.remove(value)
print(arr)

# solution 2
zeros = 0
nums = list()
for i in arr:
    if i!=0:
        nums.append(i)
    else:
        zeros+=1
for value in range(zeros):
    nums.append(0)

print(nums)


