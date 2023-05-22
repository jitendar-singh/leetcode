# Find Missing Number: Write a Python program to find the missing number from a given list of consecutive numbers.

def missingNumber(numbers):
    for number in numbers:
        if number+1 not in numbers:
            return number+1
    return None

if __name__ == "__main__":
    numbers = [1, 2, 3,4, 6, 7]
    print(missingNumber(numbers))