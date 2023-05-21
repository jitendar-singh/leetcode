# List Comprehension: Write a Python program to create a new list containing the squares of even numbers from a given list.

def square_of_evens(numbers):
    return [num ** 2 for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
print(square_of_evens(numbers))