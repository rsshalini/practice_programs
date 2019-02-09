#! usr/bin/python



       
def two_sum_target(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            sum_two = numbers[i] + numbers[j]
            if sum_two == target:
                if j > i:
                    return [i, j]


if __name__ == "__main__":        
    numbers=[7, 2, 11, 15]
    target=22
    print two_sum_target(numbers, target)
