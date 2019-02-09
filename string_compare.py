#! usr/bin/python

#Compare two strings A and B, determine whether A contains all of the characters in B.

#For A = "ABCD", B = "ACD", return true.
#For A = "ABCD", B = "AABC", return false.

def string_compare(A,B):
    list_A = list(A)
    list_B = list(B)
    for each_char in list_B:
        try:
            list_A.remove(each_char)
        except ValueError:
            return False
    return True
    #print list_A


if __name__ == "__main__":
    A = "AEBCD"
    B = "ACDE"
    print string_compare(A,B)