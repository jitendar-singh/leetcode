def is_anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()
    
    # return sorted(s1) == sorted(s2)

    count = {}

    for char in s1:
        if char in count:
            count[char]+=1
        else:
            count[char] = 1
    print(count)
    for char in s2:
        if char in count:
            count[char]-=1
        else:
            count[char] = 1
    print(count)
    for key, values in count.items():
        if values != 0:
            return False
    return True

s1 = 'public relations'
s2 = 'crap built on ies'
print(is_anagram(s1,s2))