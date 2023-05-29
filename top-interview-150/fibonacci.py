def fibonacci(n):
    fib_seq = [0, 1]  # Initialize the Fibonacci sequence with the first two terms

    if n <= 2:
        return fib_seq[:n]  # Return the requested number of terms

    while len(fib_seq) < n:
        next_term = fib_seq[-1] + fib_seq[-2]  # Calculate the next term
        fib_seq.append(next_term)  # Add the next term to the sequence

    return fib_seq

num_terms = 10
fibonacci_sequence = fibonacci(num_terms)
print(fibonacci_sequence)