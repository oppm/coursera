# Uses python3
import sys

def edit_distance(s, t):
    M = len(s)+1
    N = len(t)+1
    a = [ [0] * N for _ in range(M)]

    for m in range(M):
        a[m][0] = m
    for n in range(N):
        a[0][n] = n

    for m in range(1, M):
        for n in range(1, N):
            if s[m-1] == t[n-1]:
                a[m][n] = a[m-1][n-1]
            else:
                a[m][n] = a[m-1][n-1]+1
            if a[m-1][n]+1 < a[m][n]:
                a[m][n] = a[m-1][n]+1
            if a[m][n-1]+1 < a[m][n]:
                a[m][n] = a[m][n-1]+1

    return a[M-1][N-1]

def test(s1, s2, k):
    print("passed" if edit_distance(s1, s2) == k else "failed")

def unit_test():
    test("ab", "ab", 0)
    test("short", "ports", 3)
    test("editing", "distance", 5)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        unit_test()
    else:    
        print(edit_distance(input(), input()))
