def fibonacci_sum():
    fibonacci = [0, 1]
    for _ in range(2, 50):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fibonacci_sum = sum(fibonacci)
    return fibonacci_sum

result = fibonacci_sum()
print("Sum of the first 50 Fibonacci numbers:", result)