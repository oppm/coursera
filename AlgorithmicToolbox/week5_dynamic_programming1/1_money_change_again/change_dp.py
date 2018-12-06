# Uses python3
import sys

def get_change(m):
    #write your code here
    
    a = [0 for i in range(4)]
    denom = [1, 3, 4]
    min_num_coins = 0

    for b in range(1, m+1):
        min_num_coins += 1
        for d in denom:
            if b >= d:
                d_i = (b-d) % 4
                num_coins = a[d_i]+1
                if min_num_coins > num_coins:
                    min_num_coins = num_coins
        a[b % 4] = min_num_coins

    return a[m % 4]

def single_test(m, coins):
    print("passed" if get_change(m) == coins else "failed")

def unit_test():
    single_test(2, 2)
    single_test(34, 9)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:
        m = int(sys.stdin.read())
        print(get_change(m))