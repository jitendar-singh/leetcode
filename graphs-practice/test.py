str1 = "hello sunny singh whats up"

str1 = str1.lower().replace(' ', '')
count = {}

# for char in str1:
#         char_freq1[char] = char_freq1.get(char,0) + 1

for char in str1:
    count[char] = count.get(char,0) + 1

print(count)
