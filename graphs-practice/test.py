from collections import Counter
str1 = "hello sunny singh whats up"

str1 = str1.lower().replace(' ', '')
count = {}

# for char in str1:
#         char_freq1[char] = char_freq1.get(char,0) + 1

for char in str1:
    count[char] = count.get(char,0) + 1

print(count)
l = [0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1]
out = Counter(l)
for i in range(out[1]):
    l.remove(1)
for i in range(out[1]):
    l.append(1)
print(l)

