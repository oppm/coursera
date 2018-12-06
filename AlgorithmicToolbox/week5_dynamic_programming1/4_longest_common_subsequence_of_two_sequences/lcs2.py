#Uses python3

import sys

def lcs2(s, t):
    M = len(s)+1
    N = len(t)+1

    a = [[0] * N for _ in range(M)]

    for m in range(1, M):
        for n in range(1, N):
            if s[m-1] == t[n-1]:
                max = a[m-1][n-1] + 1
            else:
                if a[m][n-1] > a[m-1][n]:
                    max = a[m][n-1]
                else:
                    max = a[m-1][n]

            a[m][n] = max

    return a[M-1][N-1]
    

def test(a, b, n):
    print("passed" if lcs2(a, b) == n else "failed")

def unit_test():
    test([2, 7, 5], [2, 5], 2)
    test([7], [1, 2, 3, 4], 0)
    test([2, 7, 8, 3], [5, 2, 8, 7], 2)
    test([1, 2, 3, 4], [5, 6, 7, 8], 0)
    test([1, 1, 1, 1], [1, 1], 2)
    test([6, 5, 4, 3], [3, 2], 1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:       
        input = sys.stdin.read()
        data = list(map(int, input.split()))

        n = data[0]
        data = data[1:]
        a = data[:n]

        data = data[n:]
        m = data[0]
        data = data[1:]
        b = data[:m]

        print(lcs2(a, b))
