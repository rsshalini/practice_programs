#! usr/bin/python

# Reverse a 3-digit integer.

# Example
# Reverse 123 you will get 321.

# Reverse 900 you will get 9.

def reverse_3d_integer(num):
    a = num[::-1]
    return int(a)



if __name__ == '__main__':
    num = raw_input("Enter a 3 digit number:")
    print reverse_3d_integer(num)