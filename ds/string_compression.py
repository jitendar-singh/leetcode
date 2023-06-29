def compress(s):
    index, length, i,output = {}, len(s), 0, ''

    while i < length:
        if s[i] not in index:
            index[s[i]]=1
        else:
            index[s[i]]+=1
        i+=1
    for key,value in index.items():
        output=output+(key+str(value))
    return output

s = 'AABBCCCDDD'
print(compress(s))




    