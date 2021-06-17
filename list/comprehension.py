squares = []

for x in range(10):
    squares.append(x**2)

print(squares)

cubes = [x**3 for x in range(10)]
print(cubes)

tuples = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(tuples)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit = [fruit.strip() for fruit in freshfruit]
print(freshfruit)

# create a list of 2-tuples like (number, square)
print([(x,x**2) for x in range(5)])

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([item for num in vec for item in num])



