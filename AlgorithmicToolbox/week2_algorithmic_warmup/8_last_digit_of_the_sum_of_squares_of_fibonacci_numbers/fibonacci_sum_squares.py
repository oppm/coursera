# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def calc_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return a, b

def fibonacci_sum_squares(n):
    if n == 0:
        return 0
    a,b = calc_fib((n-1) % 60)
    return (b*(a+b)) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
