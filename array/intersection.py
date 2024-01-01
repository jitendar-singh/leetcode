# Find the intersection of two arrays.

def find_intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    intersection = set1.intersection(set2)

    result = list(intersection)

    return result

array1 = [1, 2, 2, 1, 3, 4, 5, 6]
array2 = [2, 2, 3, 5, 6]

intersection_result = find_intersection(array1, array2)
print(f"The intersection of the two arrays is: {intersection_result}")

