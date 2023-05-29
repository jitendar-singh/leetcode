def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def isCoprime(num1, num2):
    return gcd(num1, num2) == 1

# Example usage:
num1 = 100
num2 = 20

if isCoprime(num1, num2):
    print(f'{num1} and {num2} are coprimes')
else:
    print(f'{num1} and {num2} are not coprimes')