def duplicate(nums):
    count = {}

    for num in nums:
        if num in count:
            return num
        count[num] = 1
        print(count)

nums = [1,3,4,2,2,3,3]
print(f"Duplicate numbers are : {duplicate(nums)}" )