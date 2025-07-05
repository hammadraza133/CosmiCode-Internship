def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

num = int(input("Enter a number: "))
print(f"Prime factors of {num}: {prime_factors(num)}")
