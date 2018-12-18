# Uses python3
import sys
import itertools

def partition3_brute_force(A):
    s = sum(A[k] for k in range(len(A)))
    if s % 3 > 0:
        return 0

    partial_sum = s // 3
    
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        sums[0] = sum(A[k] for k in range(len(A)) if c[k] == 0)
        if sums[0] == partial_sum:
            sums[1] = sum(A[k] for k in range(len(A)) if c[k] == 1)
            if sums[1] == partial_sum:
                sums[2] = sum(A[k] for k in range(len(A)) if c[k] == 2)
                if sums[2] == partial_sum:
                    return 1
    return 0

def partition3(A):
    return partition3_brute_force(A)

def test(A, res):
    print("passed" if partition3_brute_force(A) == res else "failed")

def unit_test():
    test([3, 3, 3, 3], 0)
    test([40], 0)
    test([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 1)
    test([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:            
        input = sys.stdin.read()
        n, *A = list(map(int, input.split()))
        print(partition3(A))

