# Uses python3
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return a

n = int(input())
print(calc_fib(n))
