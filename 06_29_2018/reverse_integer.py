#! usr/bin/python
#Write a program to reverse a 3digit integer




#above gives a string. reverse operation can only be done on a string

#function below reverses the integer
def reverse_integer(num):
    try:
        return int(num[::-1])
    except ValueError:
        return "Try entering an integer. no alphabets"

print reverse_integer(raw_input("Enter a 3 digit integer:"))