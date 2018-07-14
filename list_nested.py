#! usr/bin/python


def is_list(p):
    return isinstance(p,list)


#c = [1,[2,3,7],9,[4,5],6]


def remove_nested_in_list(a_list):
    new_list = []
    for item in a_list:
        if is_list(item):
            a_list.extend(item)
        else:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    a = [4,[3,[2,[1]]]]
    print remove_nested_in_list(a)