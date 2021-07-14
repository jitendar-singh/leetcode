def sqaure(num: int)-> int:
    return num * num

def cubes(num: int)-> int:
    return num * num * num

def my_map(func,args_list):
    results = []

    for nums in args_list:
        results.append(func(nums))
    return results

arr = [1,2,3,4,5]
sqaures = my_map(sqaure,arr)
cubes = my_map(cubes,arr)
print(sqaures)
print(cubes)