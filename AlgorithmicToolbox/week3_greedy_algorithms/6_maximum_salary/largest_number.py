#Uses python3

import sys

def compare(a, b):
    i = 1
    ab = a+b
    ba = b+a

    for i in range(len(ab)):
        digit_ab = int(ab[i])
        digit_ba = int(ba[i])

        if digit_ab != digit_ba:
            return digit_ab > digit_ba
    
    return True # equal

def largest_number(a):
    #write your code here
    res = ""
    
    while len(a) > 0:
        max = "0"
        for x in a:
            if compare(x, max):
                max = x
        res += max
        a.remove(max)
    
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
