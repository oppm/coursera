# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def calc_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return a            

def get_fibonacci_sum(n):
    m = n + 2
    m = m % 60
    return (calc_fib(m)-1)

def fibonacci_partial_sum(m, n):
    a = get_fibonacci_sum(n)
    b = get_fibonacci_sum(m-1)

    return (a-b) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))