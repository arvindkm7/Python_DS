#  Using pop() funtion

# def rotate_pop(arr):
#     last_num = arr[-1]
#     arr.pop()
#     arr[0] = last_num
#     return arr

# arr = [1, 2, 3, 4, 5, 6]
# print(rotate_pop(arr))

# using for loop

def rotate(arr, n):
    if not arr:
         return arr
    count = 1
    while count <= n:
        last = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i]=arr[i-1]
        arr[0] = last
        count += 1
        print (arr)
    return arr

arr = [1, 2, 3, 4, 5, 6]
n = int(input('Enter the rotate no : '))
print(f'Array after rotation {rotate(arr, n)}')