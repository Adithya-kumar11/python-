def even_numbers_up_to(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num


for even_num in even_numbers_up_to(10):
    print(even_num)