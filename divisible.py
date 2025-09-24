def divisible_by_3_and_5():
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append(num)
    return result

print("Numbers between 1 and 100 divisible by both 3 and 5:")
print(divisible_by_3_and_5())
