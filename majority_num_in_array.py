#! usr/bin/python

def majority_num_in_array(num_array):
    d = dict()
    for each_num in num_array:
        if each_num not in d.keys():
            d[each_num] = 1
        elif each_num in d.keys():
            d[each_num] += 1
    
    #returns the key where the value is maximum
    key_max_value = max(d, key = d.get)

    measure_percent = float(d[key_max_value]) / len(num_array)
    
    if measure_percent > 0.5:
        return key_max_value
    else:
        return "no majority number. try with another array"


if __name__ == "__main__":
    num_array = [1, 1, 1, 1, 2, 2, 2]
    print majority_num_in_array(num_array)