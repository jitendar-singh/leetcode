def find_kth_largest_element(arr, k):
    while True:
        distinct_values = set(arr)
        new_elements = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                new_element = abs(arr[i] - arr[j])
                if new_element not in distinct_values:
                    new_elements.append(new_element)
        if not new_elements:
            break
        arr.extend(new_elements)
    
    arr.sort(reverse=True)
    
    if k <= len(arr):
        return arr[k - 1]
    else:
        return -1

# Example usage
array = [3, 7, 10]
k = 2

result = find_kth_largest_element(array, k)
print(f"The kth largest element is: {result}")
