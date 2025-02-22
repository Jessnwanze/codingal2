import time
import sys

def constant_time(n):
    return n * 2  # O(1)

def logarithmic_time(n):
    i = 1
    while i < n:
        i *= 2  # O(log n)

def linear_time(n):
    for i in range(n):
        pass  # O(n)

def quadratic_time(n):
    for i in range(n):
        for j in range(n):
            pass  # O(n^2)

def exponential_time(n):
    if n == 0:
        return 1
    return exponential_time(n - 1) + exponential_time(n - 1)  # O(2^n)

def factorial_time(n):
    if n == 0:
        return 1
    return n * factorial_time(n - 1)  # O(n!)

def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

def measure_space(func, *args):
    before = sys.getsizeof(args)
    func(*args)
    after = sys.getsizeof(args)
    return after - before

n = 10
print("Time Complexity Analysis:")
print(f"Constant Time O(1): {measure_time(constant_time, n)} sec")
print(f"Logarithmic Time O(log n): {measure_time(logarithmic_time, n)} sec")
print(f"Linear Time O(n): {measure_time(linear_time, n)} sec")
print(f"Quadratic Time O(n^2): {measure_time(quadratic_time, n)} sec")

# Avoid running exponential and factorial functions for large values
print(f"Exponential Time O(2^n): {measure_time(exponential_time, 5)} sec")
print(f"Factorial Time O(n!): {measure_time(factorial_time, 5)} sec")

print("\nSpace Complexity Analysis:")
print(f"Linear Space O(n) Example: {measure_space(linear_time, n)} bytes")
