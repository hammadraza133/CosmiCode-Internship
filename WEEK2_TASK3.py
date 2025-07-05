def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"GCD of {x} and {y} is: {gcd(x, y)}")
print(f"LCM of {x} and {y} is: {lcm(x, y)}")
