def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10   # Get last digit
        num //= 10          # Remove last digit
    return total

n = int(input("Enter a number: "))
print(f"Sum of digits of {n} is {sum_of_digits(n)}")