# Task 4: Area of Trapezoid and Ellipse

def area_trapezoid(a, b, h):
    return 0.5 * (a + b) * h

def area_ellipse(a, b):
    import math
    return math.pi * a * b

print("Area of Trapezoid")
a = float(input("Enter base 1: "))
b = float(input("Enter base 2: "))
h = float(input("Enter height: "))
print(f"Area of trapezoid is: {area_trapezoid(a, b, h)}")

print("\nArea of Ellipse")
x = float(input("Enter semi-major axis (a): "))
y = float(input("Enter semi-minor axis (b): "))
print(f"Area of ellipse is: {area_ellipse(x, y)}")
