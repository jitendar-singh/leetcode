# Implement an algorithm to find duplicates in an array

def find_duplicates(arr):
    index = dict()
    duplicates = []
    for item in arr:
        if item not in index.keys():
            index[item] = 1
        else:
            duplicates.append(item)
    return set(duplicates)

print(find_duplicates([1,1,1]))