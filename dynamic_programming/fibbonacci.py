#  finding the nth Fibonacci number
def fibonacci_dynamic(n):

    cache  = {}

    def fibbonaci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = fibbonaci(n - 1) + fibbonaci(n - 2)
        
        cache[n] = result
        return result

    return fibbonaci(n)

# Testing the dynamic programming approach
print(fibonacci_dynamic(10))  # Output: 55
print(fibonacci_dynamic(20))  # Output: 6765
print(fibonacci_dynamic(30))  # Output: 832040




