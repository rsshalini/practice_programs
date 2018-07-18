#! usr/bin/python

#Given an array of integers and a number k, the majority number is the number that occurs more than 1/k of the size of the array.
#Given [3,1,2,3,2,3,3,4,4,4] and k=3, return 3.



def majority_number_1byk(arr,k):
    arr_dict = {}
    for digit in arr:
        if digit not in arr_dict:
            arr_dict[digit] = 1
        elif digit in arr_dict:
            arr_dict[digit] += 1

    majority_value = len(arr)/float(k)

    #print arr_dict
    #print int(round(majority_value))

    for key, value in arr_dict.iteritems():
        if value > majority_value:
            return key
    
if __name__ == "__main__":
    arr = [3,1,2,3,2,3,3,4,4,4]
    k = 3
    print majority_number_1byk(arr,k)

