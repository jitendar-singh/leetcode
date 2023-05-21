# Problem: Square Numbers
# Write a Python program that takes a list of numbers as input and returns a new list containing the squares of each number.
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]

def square_of_nums(numbers):
    return [num ** 2 for num in numbers]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(square_of_nums(numbers))

