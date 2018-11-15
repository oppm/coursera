# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def calc_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return a            

def get_fibonacci_huge(n):
    m = n + 2
    m = m % 60
    return (calc_fib(m)-1) % 10

def fibonacci_sum(n):
    return get_fibonacci_huge(n) 

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)    
    print(fibonacci_sum(n))
