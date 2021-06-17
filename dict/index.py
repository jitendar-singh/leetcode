tel = {'jack': 4098, 'sape': 4139, 'sunny': 9513}
print(tel['jack'])
print(tel)
print(list(tel))
print(sorted(tel))

for k, v in tel.items():
    print(k,':',v)

for k,v in enumerate(tel):
    print(k,':',v,':',tel[v])