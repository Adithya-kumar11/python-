def print_args_kwargs(*args, **kwargs):
    print("Arguments (args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword Arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_args_kwargs(10, 20, 30, name="Adithya", age=22, city="Bhadrachalam")