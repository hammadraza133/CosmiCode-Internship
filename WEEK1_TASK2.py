# Task 2: Advanced Arithmetic Operations

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"{x} to the power {y} is: {power(x, y)}")
print(f"{x} modulo {y} is: {modulo(x, y)}")
