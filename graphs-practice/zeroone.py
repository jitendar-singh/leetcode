from collections import Counter
l = [0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1]
count = Counter(l)
output = []
for key, value in count.items():
    for i in range(value):
        output.append(key)
print(output)
print(count)
print(Counter(output))


