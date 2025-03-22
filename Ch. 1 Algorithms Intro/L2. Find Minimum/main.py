def find_minimum(nums):
    minimum = float("inf")
    if len(nums) < 1:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
