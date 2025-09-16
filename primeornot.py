def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False
    # Check divisibility from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = 61
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

