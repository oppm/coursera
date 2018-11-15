# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_pisano_period(m):
    a = 0
    b = 1
    i = 0
    while True:
        i = i + 1
        n = a + b
        n = n % m
        a = b
        b = n
        if a == 0 and b == 1:
            return i    

def calc_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return a            

def get_fibonacci_huge(n, m):
    pisano_perdiod = get_pisano_period(m)
    n = n % pisano_perdiod
    return calc_fib(n) % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
