def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements

    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n

    return second if second != float('-inf') else None

print(second_largest([32,36,46,56,61]))