def duplicate(nums):
    count = {}
    dup = []

    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num, count in count.items():
        if count > 1:
            dup.append(num)    
    return dup


nums = [1,3,4,2,2,3,3]
print(f"Duplicate numbers are : {duplicate(nums)}" )