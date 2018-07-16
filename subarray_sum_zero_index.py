#! usr/bin/python

# Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

# Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

#a = [-3, 1, 2, -3, 4]


def subarray_sum_zero_index(arr):
    for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        sub_arr = arr[i:j]
        if sum(sub_arr) == 0 and len(sub_arr) > 0:
           return [i, j-1]


if __name__ == "__main__":
    arr = [-3, 1, 2, -3, 4]
    print subarray_sum_zero_index(arr)