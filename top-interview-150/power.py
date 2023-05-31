# Python program that calculates the power of an integer raised to the nth value:

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base # 2 , 4 , 8 , 16, 32
    return result

# Example usage:
base = 2
exponent = 5

result = power(base, exponent)
print(f"The result of {base} raised to the power of {exponent} is: {result}")  # Output: The result of 2 raised to the power of 5 is: 32