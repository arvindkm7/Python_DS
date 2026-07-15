def sum_sub_arr(arr):
    large_sum, cur_sum, i, j, k = 0, 0, 0, 1, 2
    large_lst = []
    
    for i in range(0, len(arr) - 3):
        cur_sum = arr[i] + arr[j] + arr[k]

        if cur_sum >= large_sum:
            large_sum = cur_sum
            if len(large_lst) == 0:
                large_lst.append(arr[i])
                large_lst.append(arr[j])
                large_lst.append(arr[k])
            else:
                large_lst.clear()
                large_lst.append(arr[i])
                large_lst.append(arr[j])
                large_lst.append(arr[k])
        j += 1
        k += 1
        # print(f'large_lst : {large_lst}, large_sum :{large_sum }')
    return large_lst
        
arr = [-1, 5, 6, -5, -6, 5, -8, 5, 6, 7, -5]
print(sum_sub_arr(arr))
