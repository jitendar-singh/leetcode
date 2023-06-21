# from typing import Counter

def countoccurance(str1):
    output = ""
    count = 1
    for char in range(1, len(str1)):
        if str1[char] == str1[char - 1]:
            count+=1
        else:
            output+=str1[char-1]+str(count)
            count = 1
    output+=str1[-1]+str(count)
    return  output

s = 'qqqrttttnnnqppzss'
print(countoccurance(s))
