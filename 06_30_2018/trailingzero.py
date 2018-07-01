#!usr/bin/python

#counts the number of trailing zero for n factorial

import math
def count_trailing_zero_n_fact(n):
    n_factorial = str(math.factorial(n))
    trailing_zero_count = 0
    if n_factorial.endswith('0'):
        for i in reversed(n_factorial):
            #print "i", i
            if i == '0':
                trailing_zero_count += 1
                #print "ct", trailing_zero_count
            else:
                break
        return "Number of trailing zero in {0} factorial {1} is {2}".format(n, n_factorial,trailing_zero_count)       
    else:
        return "No trailing zeros in {0} factorial".format(n)

if __name__ == "__main__":
    n = int(raw_input("Enter an integer:"))
    print count_trailing_zero_n_fact(n)


