#! usr/bin/python

# Given an array of integers, find the subarray with smallest sum.

# Return the sum of the subarray.

# For [1, -1, -2, 1], return -3.
#[1, -5, -2, 1]





def min_sum_sub_array(arr):   
    min_so_far = 0 
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            sub_list = arr[i:j]
            #print sum(sub_list)
            if sum(sub_list) < min_so_far:
                min_so_far = sum(sub_list)
    return min_so_far

if __name__ == "__main__":
    arr = [1, -5, -2, 1]
    print min_sum_sub_array(arr)

