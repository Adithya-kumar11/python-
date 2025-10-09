class NumberUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0


print(NumberUtils.is_even(4))  # True
print(NumberUtils.is_even(7))  # False