def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    temp = arr[:k]

    for i in range(k,n):
        arr[i-k] = arr[i]
    
    for i in range(n-k, n):
        arr[i] = temp[i-(n-k)]

my_array = [1, 2, 3, 4, 5]
rotate_array(my_array, 1)
print(my_array) 