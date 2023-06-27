# 1,2,3
# 4,5,6
# 7,8,9

# x = 1 , y = 2 sum = 1+2+3+4+5+6

def sumxy(arr,x,y):
    xy, s = [], 0
    for i in range(x):
        for j in range(y):
            xy.extend(arr[j])
    for items in xy:
        s+=items
    return s


arr = [[1,2,3],[4,5,6],[7,8,9]]
print(sumxy(arr,1,1))