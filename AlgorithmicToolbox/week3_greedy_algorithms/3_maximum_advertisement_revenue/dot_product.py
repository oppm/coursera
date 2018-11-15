#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        a_max = -10**6
        a_max_i = 0
        b_max = -10**6
        b_max_i = 0
        for j, an in enumerate(a):
            if an > a_max:
                a_max = an
                a_max_i = j
        for j, bn in enumerate(b):
            if bn > b_max:
                b_max = bn
                b_max_i = j
        res += (a_max*b_max)
        a[a_max_i] = -10**6
        b[b_max_i] = -10**6

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
