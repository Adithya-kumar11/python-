def my_max(iterable):
    #assume iterable is non-empty
    maximum = iterable[0]     #start with first element
    for item in iterable[1:]:
        if item >  maximum:
            maximum = item
    return maximum
nums =[32,36,46,56,61]
print(my_max(nums))