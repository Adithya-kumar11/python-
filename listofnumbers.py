def remove_duplicate(nums):
    result = []
    for n in nums:
        if n not in result:
             result.append(n)  
    return result
numbers = [1,3,5,7,9] 
print(remove_duplicate(numbers))      