#! usr/bin/python

# Find K-th largest element in an array.

# In array [9,3,2,4,8], the 3rd largest element is 4.

# In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.


def k_largest_element(arr, k):
    #sorts the array from largest to smallest
    arr.sort(reverse = True)
    #assuming the user won't give based on zero index
    kth_element = k-1
    return arr[kth_element]

if __name__ == "__main__":
    arr = [9,3,2,4,8]
    k = 4
    print k_largest_element(arr,k)