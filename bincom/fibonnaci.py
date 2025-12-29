""" 9. Write a program to sum the first 50 fibonacci sequence. """

def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for i in range(n):
        total += a
        a, b = b, a + b
    return total

fib_sum = fibonacci_sum(50)
print(f"\n9. Sum of first 50 Fibonacci numbers: {fib_sum}")