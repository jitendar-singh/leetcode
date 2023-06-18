def fibonacci(number):
    arr = [0] * number
    arr[0] = 0
    arr[1] = 1

    for i in range(2,number):
        arr[i] = arr[i - 1 ] + arr[i - 2]
    return arr

arr = fibonacci(20)
print(arr)