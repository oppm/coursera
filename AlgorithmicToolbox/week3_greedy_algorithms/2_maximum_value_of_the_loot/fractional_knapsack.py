# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_weight = [values[i] / weights[i] for i in range(len(values))]
    nvalues = len(values)

    while capacity > 0 and nvalues > 0:
        vw_max = 0
        i_max = 0
        for i, vw in enumerate(value_per_weight):
            if vw > vw_max:
                i_max = i
                vw_max = vw
        
        if capacity > weights[i_max]:
            capacity -= weights[i_max]
            value += values[i_max]
            value_per_weight[i_max] = 0
        else:
            value += (capacity * value_per_weight[i_max])
            capacity = 0
        nvalues -= 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
