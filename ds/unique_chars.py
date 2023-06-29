def unique(s):
    i, index, length = 0, {}, len(s)

    while i < length:
        if s[i] not in index:
            index[s[i]] = 1
            i+=1
        else:
            return False
    return True

s = 'acdz'
print(unique(s))
