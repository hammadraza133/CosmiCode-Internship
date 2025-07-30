def complex_calculation(a, b):
    try:
        result = (a ** 2 + b ** 2) / (a - b)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except TypeError:
        print("Error: Invalid input type.")
    except Exception as e:
        print("An unexpected error occurred:", e)

complex_calculation(5, 5)  # Will cause division by zero
