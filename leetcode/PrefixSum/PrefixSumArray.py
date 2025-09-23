arr = [1,5,8,2,6,7 ]
prefix_sum_array = [0]*len(arr)
prefix_sum_array[0] = arr[0]

for i in range(1, len(arr)):
    prefix_sum_array[i] = prefix_sum_array[i-1] + arr[i]

print(prefix_sum_array)
