

def fizz_bizz(n):
    if n%3 == 0 and n%5==0:
        return "fizz buzz"
    elif n%5 == 0:
        return "buzz"
    elif n%3 == 0:
        return "fizz"
    else:
        return n

if __name__ == "__main__":
    n = raw_input("Enter an integer:")
    ans = []
    for digit in range(1,int(n)):
        ans.append(fizz_bizz(int(digit)))
    print ans

