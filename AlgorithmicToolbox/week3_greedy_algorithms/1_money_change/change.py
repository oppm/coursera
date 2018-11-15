# Uses python3
import sys

def get_change(m):
    denom = [10, 5, 1]
    denom_i = 0
    n = 0

    #while m > 0:
    #    while m >= denom[denom_i]:
    #        n += 1
    #        m -= denom[denom_i]
    #    denom_i += 1

    while m > 0:
        a = m // denom[denom_i]
        b = m % denom[denom_i]
        n += a
        m = b
        denom_i += 1

    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
