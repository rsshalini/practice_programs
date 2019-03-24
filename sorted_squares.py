
#https://leetcode.com/problems/squares-of-a-sorted-array/
#squares of sorted array

def sortedSquares(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    #take mod of the numbers
    #sort it
    #then caclulate squares
    abs_num = []
    for i in A:
        if i <0:
            abs_num.append(abs(i))
        else:
            abs_num.append(i)
    
    abs_num.sort()
            
    squared_list = []
    for i in abs_num:
        squared_list.append(i*i)
    
    return squared_list

#example 1
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

#example 2
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]