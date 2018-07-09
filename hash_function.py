#! usr/bin/python

# hashcode("abcd") = (ascii(a) * 33^3 + ascii(b) * 332^ + ascii(c) *33^1 + ascii(d) * 33^0) % HASH_SIZE 

#                               = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

#                               = 3595978 % HASH_SIZE

# here HASH_SIZE is the capacity of the hash table (you can assume a hash table is like an array with index 0 ~ HASH_SIZE-1).

# Given a string as a key and the size of hash table, return the hash value of this key.


def hashcode_num(hash_size, key):
    hashcode_1 = 0
    for index, char in enumerate(reversed(key)):
        hashcode_1 += ord(char) * pow(33,index)
    return hashcode_1 % hash_size


if __name__ == "__main__":
    hash_size = int(raw_input("Enter a integer for hash size:"))
    key_string = raw_input("Enter a string:")
    print hashcode_num(hash_size,key_string)

