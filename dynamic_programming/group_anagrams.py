# Given an array of strings, group anagrams together

def group_anagram(arr):
    group = {}
    for i in range(len(arr)):
        previous = ''.join(sorted(arr[i]))
        for j in range(i+1,len(arr)):
            next_item = ''.join(sorted(arr[j]))
            if is_anagram(previous,next_item):
                if arr[j] not in group:
                    group[arr[i]] = arr[j]
    return group

def is_anagram(previous, next_item):
    if previous == next_item:
            return True

arr = ["eat", "tea", "tan", "ate", "bat", "nat"]
print(group_anagram(arr))