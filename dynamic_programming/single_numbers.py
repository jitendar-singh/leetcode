def single_numbers(arr):
    count = {}
    for number in arr:
        if number in count:
            count[number]+=1
        else:
            count[number]=1
    for key, value in count.items():
        if value == 1:
            return key
    return None
arr = [2,2,3,3,3,0,1,1,4,4,5,5]
print(single_numbers(arr))