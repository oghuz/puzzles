#!/usr/bin/env python

import sys

mapping = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', \
           10:'ten', 11: 'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', \
           17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', \
           60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 1000:'thousand', 1000000:'million', 1000000000:'billion'}

def simple_convert(number):
    global mapping
    if number ==0:
        return None
    if number in mapping:
        return mapping[number]
    composition = []
    if number >=100:
        digit = number/100
        composition.append(mapping[digit])
        composition.append('hundred')
        rest = simple_convert(number%100)
        if rest:
            composition.append(rest)
    else: # number falls into range[0,99]
        digit = (number/10)*10
        composition.append(mapping[digit])
        composition.append(simple_convert(number%10))

    return ' '.join(composition) 

def convert(number):
    return simple_convert(number %1000)

def main():
    while True:
        try:
            num = int(raw_input('Input number:'))
        except ValueError:
            print "Input is NOT a number"
            return 1
        if num ==0:
            print "%d --> %s" % (num, mapping[num])
        elif num >0:
            print "%d --> %s" % (num, convert(num))
        else:
            break
            # print "%d --> Minus %s" % (num, convert(num))


if __name__ == '__main__':
    main()

