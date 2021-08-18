from typing import Counter


s = 'qqqrttttnnnqppzss'
# output = q3r1t4n3q1p2z1s2
counter = 0
for i in range(len(s)):
    current = s[i]
    counter+=1
    if s[i+1] == current:
        counter+=1
    else:
        output = current+str(counter)
print(output)