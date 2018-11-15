# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_step(a, b):
    #print("a: {0}, b: {1}\n".format(a, b))
    if a == b:
        return a

    r = a % b

    if r == 0:
        return b
    if r == 1:
        return 1

    return gcd_step(b, r)

def gcd(a, b):    
    if a > b:
        return gcd_step(a, b)
    else:
        return gcd_step(b, a)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
