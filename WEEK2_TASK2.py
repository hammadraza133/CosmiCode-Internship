# Iterative
def fibonacci_iterative(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Recursive
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print("First 30 Fibonacci numbers (iterative):")
print(fibonacci_iterative(30))

print("\nFirst 30 Fibonacci numbers (recursive):")
for i in range(30):
    print(fibonacci_recursive(i), end=" ")
