#Uses python3

import sys

def lcs3(a, b, c):
    M = len(a)+1
    N = len(b)+1
    O = len(c)+1

    T = [[[0 for _ in range(O)] for _ in range(N)] for _ in range(M)]

    for m in range(1, M):
        for n in range(1, N):
            for o in range(1, O):
                if a[m-1] == b[n-1] and a[m-1] == c[o-1]:
                    max = T[m-1][n-1][o-1] + 1
                else:
                    x = T[m-1][n][o]
                    y = T[m][n-1][o]
                    z = T[m][n][o-1]
                    max = x if x >= y and x >= z else y if y >= x and y >= z else z

                T[m][n][o] = max

    return T[M-1][N-1][O-1]

def test(a, b, c, n):
    print("passed" if lcs3(a,b,c) == n else "failed")

def unit_test():
    test([1,2,3],[2,1,3],[1,3,5], 2)
    test([8,3,2,1,7],[8,2,1,3,8,10,7],[6,8,3,1,4,7], 3)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:           
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        an = data[0]
        data = data[1:]
        a = data[:an]
        data = data[an:]
        bn = data[0]
        data = data[1:]
        b = data[:bn]
        data = data[bn:]
        cn = data[0]
        data = data[1:]
        c = data[:cn]
        print(lcs3(a, b, c))
