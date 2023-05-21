# Problem: Even Numbers
# Write a Python program that takes a list of numbers as input and returns a new list containing only the even numbers from the input list.
# Example:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [2, 4, 6, 8]

def even_nums(numbers):
    return [number for number in numbers if number % 2 == 0]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(even_nums(numbers))

