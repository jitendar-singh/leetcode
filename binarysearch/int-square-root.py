def integer_square(key: int) -> int:
    # key = 300
    # 17^2 = 289 < 300. Note 18^2 = 324 > 300.
    # So the number 17 is the correct response
    # low = 0
    # high = key
    # mid = (low + high) // 2
    # if (mid ** 2) > key:
    #     high = mid - 1
    # elif (mid ** 2) < key:
    #     low = mid + 1
    # else:
    #     return mid
    ds = {}
    while(True):
        for i in range(key):
            ds[i] = i**2
            if ds[i] == key:
                val = ds[i]
            elif ds[i] > key:
                val = ds[i-1]
                break
        for k,v in ds.items():
            if v == val:
                # print(ds)
                return k
k = 325 
# k = 324 17
print(integer_square(k))

