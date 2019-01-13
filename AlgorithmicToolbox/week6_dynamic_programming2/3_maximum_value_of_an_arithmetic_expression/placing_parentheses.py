# Uses python3
import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_value(A, n):
    return int(A[n*2])

def get_op(A, n):
    return A[1+n*2]

def get_maximum_value(A):
    
    num_values = (len(A)+1)//2
    num_ops = (len(A)-1)//2

    m = [[0] * num_values for _ in range(num_values)]

    for i in range(num_values):
        m[i][i] = get_value(A, i)

    for i in range(1, num_ops+1):
        for j in range(i, num_ops+1):
            x = j - i
            y = j

            for k in range(x, y):
                op = get_op(A, k)
                max_left_value = m[x][k]
                max_right_value = m[k+1][y]
                min_left_value = m[k][x]
                min_right_value = m[y][k+1]
                a = evalt(max_left_value, max_right_value, op)
                b = evalt(max_left_value, min_right_value, op)
                c = evalt(min_left_value, max_right_value, op)
                d = evalt(min_left_value, min_right_value, op)
                if k == x:
                    max_ = max([a, b, c, d])
                    min_ = min([a, b, c, d])
                else:
                    max_ = max([max_, a, b, c, d])
                    min_ = min([min_, a, b, c, d])

            m[x][y] = max_
            m[y][x] = min_
            pass
    
    return m[0][num_values-1]

def calc(A, base):
    num_values = (len(A)+1) // 2
    num_ops = (len(A)-1) // 2

    if num_values == 1:
        return [int(A[0]), int(A[0])]

    for o in range(num_ops):

        left_side = A[:1+2*o]
        right_side = A[2+2*o:]
        op = A[1+2*o]

        [min_left, max_left] = calc_cached(left_side, base, 0)
        [min_right, max_right] = calc_cached(right_side, base+o+1, 0)

        a = evalt(max_left, max_right, op)
        b = evalt(max_left, min_right, op)
        c = evalt(min_left, max_right, op)
        d = evalt(min_left, min_right, op)

        if o == 0:
            max_ = max([a, b, c, d])
            min_ = min([a, b, c, d])
        else:
            max_ = max([max_, a, b, c, d])
            min_ = min([min_, a, b, c, d])

    return [min_, max_]

def calc_cached(A, base=0, reset=1):

    global cache_valid
    global cache_value

    num_values = (len(A)+1) // 2

    if reset == 1:
        cache_valid = [[0] * num_values for _ in range(num_values)]
        cache_value = [[0] * num_values for _ in range(num_values)]

    x = base
    y = base + num_values - 1

    if cache_valid[x][y] > 0:
        return [cache_value[y][x], cache_value[x][y]]

    [min_, max_] = calc(A, base)

    cache_valid[x][y] = 1
    cache_valid[y][x] = 1
    cache_value[x][y] = max_
    cache_value[y][x] = min_    

    return [min_, max_]

def get_maximum_value_top_down(A):
    [min_, max_] = calc_cached(A)
    return max_

def test(A, res):
    r = get_maximum_value_top_down(A)
    print("passed" if r == res else "failed ({0})".format(r))

def unit_test():
    test("1+2+3+4+5+6", 21)
    test("1+2+3+4+5", 15)
    test("1+2+3+4", 10)
    test("1+5", 6)
    test("1-1-1-1", 2)
    test("3*4*5", 60)
    test("5*4+2", 30)
    test("8-8*5-6", 16)
    test("5-8+7*4-8+9", 200)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        unit_test()
    else:      
        print(get_maximum_value(input()))
