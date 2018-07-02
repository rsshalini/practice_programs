#! usr/bin/python

#finds the greatest common divisor of A,B

#check if either number is 0
# GCD(A,B) = GCD(B,R)

def check_zero(A,B):
    if A == 0 and B != 0:
       return B
    elif A !=0 and B == 0:
       return A
    else:
        return "both not zero"

def find_gcd(A,B):
    while A != 0 and B!=0:
        num1 = max(A,B)
        num2 = min(A,B)
        c = num1%num2
        d = num2
        A = d
        B = c
        result = check_zero(A,B)
        if result == "both not zero":
            continue
        else:
            return result

#print find_gcd(100,90)
 #10
#print find_gcd(12,18)
 #6

if __name__ == '__main__':
    A = int(raw_input("Enter an integer A:"))
    B = int(raw_input("Enter an integer A:"))
    print find_gcd(A,B)           

