#! usr/bin/python

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#print fibonacci(5)

if __name__ == "__main__":
    print fibonacci(int(raw_input("Enter an integer:")))