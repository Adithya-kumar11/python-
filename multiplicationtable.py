def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
n = int(input("enter a number:"))
multiplication_table(n)