def reverse_in_place(lst):
    left, right = 0, len(lst) -1
    while left < right:
        #swap elements
        lst[left],lst[right] = lst[right],lst[left]
        left +=1
        right -= 1
        return lst
    
nums = [1,2,3,4,5]
reverse_in_place(nums)
print(nums)