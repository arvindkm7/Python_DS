
def k_small(arr, k):
    arr.sort()
    return arr[k-1]
def k_large(arr, k):
    arr.sort()
    return arr[-k]

arr = [10, 12, 15, 9, 50, 56, 58, 20, 52, 60]
k = 3

print(f"K-smallest : {k_small(arr, k)}")
print(f"K-largest : {k_large(arr, k)}")


print(f"Sorted_list : {sorted(arr)}")
