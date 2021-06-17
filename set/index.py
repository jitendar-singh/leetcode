fruits = {"banana","apple","grapes","pineapple","mango","banana"}
print(fruits)
 # fast membership testing

print("oranges" in fruits)
print('banana' in fruits)

# Demonstrate set operations on unique letters from two words
a = set('abracadabraz')
b = set('alacazam')
# unique letters in a
print(a)
# letters in a but not in b
print(a-b)
# letters in a or b or both
print(a|b)
# letters in both a and b
print(a&b)
# letters in a or b but not both
print(a ^ b)