def fibonacci(n):
    # Starting values for the Fibonacci series
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci series up to the nth term
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence[:n]

# Example usage
n = int(input("Enter the number of terms: "))
fib_series = fibonacci(n)
print(f"Fibonacci series up to {n} terms: {fib_series}")
