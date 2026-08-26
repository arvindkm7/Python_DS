arr = [2,7,11,15]
target = 9

rtype = []
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        sum = nums[i] + nums[j]
    if sum == target:
        rtype.append(i)
        rtype.append(j)
return rtype

          
        