#! usr/bin/python

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# a = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]




def min_sum_triangle(arr):
    sum = 0

    for i in range(0,len(arr)):
        min_value = min(arr[i])
        sum += min_value

    return sum

if __name__ == "__main__":
    arr = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print min_sum_triangle(arr)



