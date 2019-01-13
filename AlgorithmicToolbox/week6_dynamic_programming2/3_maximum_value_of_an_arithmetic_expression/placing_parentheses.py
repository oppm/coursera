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

def get_maximum_value(dataset):

    n_values = (len(dataset)+1) // 2
    n_ops = len(dataset) - n_values

    m = [[0] * n_values for _ in range(n_values)]

    # Diagonal
    for i in range(n_values):
        m[i][i] = int(dataset[i*2])

    for i in range(n_values-1):
        x = i
        y = i+1
        left_val = m[x][y-1]
        right_val = m[x+1][y]
        op = dataset[i*2+1]
        e = evalt(left_val, right_val, op)
        m[x][y] = e
        m[y][x] = e

    for o in range(2, n_values):
        for i in range(n_values-o):            
            x = i
            y = i+o
            left_val = m[x][y-o]
            max_right_val = m[x+1][y]
            min_right_val = m[y][x+1]
            right_val = m[x+o][y]
            max_left_val = m[x][y-1]
            min_left_val = m[y-1][x]
            left_op = dataset[2*x+1]
            right_op = dataset[2*y-1]
            a = evalt(left_val, max_right_val, left_op)
            b = evalt(left_val, min_right_val, left_op)
            c = evalt(max_left_val, right_val, right_op)
            d = evalt(min_left_val, right_val, right_op)
            max_ = max([a, b, c, d])
            min_ = min([a, b, c, d])
            m[x][y] = max_
            m[y][x] = min_

    return m[0][n_values-1]


def test(dataset, res):
    print("passed" if get_maximum_value(dataset) == res else "failed")

def unit_test():
    #test("1+5", 6)
    test("5-8+7*4-8+9", 200)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        unit_test()
    else:           
        print(get_maximum_value(input()))
