from collections import Counter
l = [0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1]

d = Counter(l)

for i in range(d[1]):
    l.remove(1)
for i in range(d[1]):
    l.append(1)
print(l)
print(d)

