# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

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

def lcm(a, b):
    return a*b//gcd(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))