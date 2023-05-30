def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, b):
    return gcd(a, b) == 1

# Example usage:
a = 15
b = 28

if is_coprime(a, b):
    print(f"{a} and {b} are coprime.")
else:
    print(f"{a} and {b} are not coprime.")


