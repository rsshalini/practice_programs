#! usr/bin/python

# Given a string and an offset, rotate string by offset. (rotate from left to right)
# Given "abcdefg".
# offset=0 => "abcdefg"
# offset=1 => "gabcdef"
# offset=2 => "fgabcde"
# offset=3 => "efgabcd"

def rotate_string(input_str, offset):
    return input_str[len(input_str)-offset:len(input_str)] + input_str[0:len(input_str)-offset]

if __name__ == "__main__":
    input_str = "abcdefg"
    offset = 2
    print rotate_string(input_str,offset)