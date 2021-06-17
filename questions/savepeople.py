
arr = [3,2,2,1,3]
limit = 3
boats = 0
arr.sort()

left = 0 
right = len(arr)-1
# print(arr[right])

while left <= right:
    if left == right:
        boats+=1
        break
    if arr[left]+arr[right]<= limit:
        boats = boats+1
        left+=1
        right-=1
    else:
        boats = boats+1
        right-=1
print(boats)


    
