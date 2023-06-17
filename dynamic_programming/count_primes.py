def count_primes_in_range(start, end):
    count = 0
    for number in range(start, end+1):
        if is_prime(number):
            count+=1

    return count

def is_prime(number):
    if number < 2:
        return False

    for i in range(2,int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

start = 1
end = 100

count = count_primes_in_range(start, end)
print(count)  # Output: 25 (there are 25 prime numbers between 1 and 100)

        
    