def is_prime(num):
    for n in range(2,num-1):
        if num % n == 0:
            return False
    return True
        
print(is_prime(7))   # Output: True
print(is_prime(12))  # Output: False
print(is_prime(29))  # Output: True
