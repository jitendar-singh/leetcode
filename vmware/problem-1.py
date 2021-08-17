a = [0,2,0,0,5,6,7,0,0,0,11,0]
b = [10,8,1,9,4,15,3]

for i in range(len(b)):
    for y in range(len(a)):
        if a[y] == 0:
            a[y]=b[i]
            break
    print(a)
print(sorted(a))