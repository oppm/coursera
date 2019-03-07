# python3
import sys

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

a_base = 99839
p = 999961

def _hash_first(pattern):
    h = 0
    x = [0] * len(pattern)
    x_i = 0
    a = 1
    for s_i, s in enumerate(pattern):
        h += (ord(s) * a) % p
        #print("{0}: {1} * {2}".format(s_i, ord(s), a))
        x[x_i] = a
        a = (a * a_base)
        x_i = (x_i+1) % len(pattern)
    return [h, x]

def _hash_next(h, s_0, s_n, x, x_i, i):
    x_prev = (x_i + len(x) - 1) % len(x)
    x_next = (x_i + 1) % len(x)
    a = (x[x_prev] * a_base)

    h -= (ord(s_0) * x[x_i])
    h += (ord(s_n) * a)
    h %= p

    #print("{0}-: {1} * {2}".format(i, ord(s_0), x[x_i]))
    #print("{0}+: {1} * {2}".format(i, ord(s_n), a))

    #assert(x[x_i] == a_base**(i-1))
    #assert(a == a_base**(i+len(x)-1))

    x[x_i] = a

    return [h, x, x_next]

def get_occurrences(pattern, text):
    [h_p, _] = _hash_first(pattern)
    res = []
    x_i = 0
    for i in range(len(text) - len(pattern) + 1):
        if i == 0:
            [h_t, x] = _hash_first(text[0:len(pattern)])
        else:
            [h_t, x, x_i] = _hash_next(h_t, text[i-1], text[i+len(pattern)-1], x, x_i, i)

        if h_p == h_t:
            if pattern == text[i:len(pattern)+i]:
                res.append(i)
        h_p = (h_p*a_base) % p
    return res

def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]    

def test(t, p):
    res_a = get_occurrences(p, t)
    res_b = get_occurrences_naive(p, t)
    print("passed" if (res_a == res_b) else "failed")

def unit_test():
    test("abacaba", "aba")
    test("Test", "testTesttesT")
    test("aaaaa", "baaaaaaa")
    test("aaa", "a")

def main():
    print_occurrences(get_occurrences(*read_input()))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:
        main()