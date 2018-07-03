#! usr/bin/python

#https://docs.cs50.net/2018/x/psets/1/credit/credit.html

#cc_num = "378282246310005"


def step_0(cc_num):
    list_step0 = []
    for i in range(1, len(cc_num),2):
        ans = int(cc_num[i])*2
        list_step0.append(str(ans))
    #print list_step0
    digits_step0 = ''.join(list_step0)

    sum_step0 = 0
    for num in digits_step0:
        sum_step0 += int(num)
    return sum_step0

def step_1(cc_num):
    sum_step1 = 0
    for j in range(0, len(cc_num),2):
        sum_step1 += int(cc_num[j])
    return sum_step1


def main(cc_num):
    step_3 = step_0(cc_num) + step_1(cc_num)
    card_identifier = cc_num[:2]
    amex = ['34','37']
    master = ['51','52', '53','54','55']
    #visa = ('4')
    if str(step_3).endswith('0'):
        if len(cc_num) == 15 and card_identifier in amex:
            return "AMEX"
        elif len(cc_num) == 16 and card_identifier in master:
            return "Master"
        elif (len(cc_num) == 13 or len(cc_num) == 16) and cc_num.startswith('4'):
            return "Visa"
    else:
        return "Invalid"




if __name__ == '__main__':
    print main(raw_input("Enter your credit card number:"))


