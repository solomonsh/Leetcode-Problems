def average_subarrays(lst):
    result = []
    for i,l1 in enumerate(lst):
        sub_array = []
        for j in range(i,len(lst)):
            temp_subarray = lst[i:j+1]
            temp_remaining = lst[:i] + lst[j+1:]
            subarray_average = sum(temp_subarray)/len(temp_subarray)
            remaining_average = 0
            if len(temp_remaining)>0:
              remaining_average =  sum(temp_remaining)/len(temp_remaining)

            if subarray_average> remaining_average:
                sub_array.append([i+1,j+1])

        result+=sub_array
    result.sort()
    return result
 

print(average_subarrays([3,4,2])==[[1, 2], [1, 3], [2, 2]])

print(average_subarrays([2]) == [[1,1]])
print(average_subarrays([2,2,2,2])==[[1,4]])

print(average_subarrays([2,2,2,1])==[[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [3, 3]])
print(average_subarrays([3,4,2,5,6]) == [[1, 5], [2, 5], [3, 5], [4, 4], [4, 5], [5, 5]])

print(average_subarrays([1,4,2,10,20,30,50,60,5,1000000])==[[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10]])