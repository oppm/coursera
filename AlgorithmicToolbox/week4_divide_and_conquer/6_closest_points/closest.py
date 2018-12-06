#Uses python3
import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(a, b):
    return math.sqrt(math.pow(a.x-b.x, 2) + math.pow(a.y-b.y, 2))

def sort(points):
    if len(points) <= 1:
        return points

    mid = len(points) // 2

    left = sort(points[:mid])
    right = sort(points[mid:])

    l = 0
    r = 0
    sorted = []
    while True:
        left_point = left[l]
        right_point = right[r]
        cmp_res = left_point.x < right_point.x if left_point.x != right_point.x else left_point.y < right_point.y
        if cmp_res:
            sorted.append(left_point)
            l += 1
            if l == len(left):
                sorted.extend(right[r:])
                break
        else:
            sorted.append(right_point)
            r += 1
            if r == len(right):
                sorted.extend(left[l:])
                break

    return sorted

def minimum_distance_analyze(sorted_by_x):
    if len(sorted_by_x) <= 1:
        a = sorted_by_x[0]
        return [float("Inf"), [a]]
    if len(sorted_by_x) <= 2:
        a = sorted_by_x[0]
        b = sorted_by_x[1]
        return [dist(a, b), [a, b] if a.y < b.y else [b, a]]

    mid = len(sorted_by_x) // 2

    left = sorted_by_x[:mid]
    right = sorted_by_x[mid:]

    [min_left, sorted_by_y_left] = minimum_distance_analyze(left)
    if min_left == 0.0:
        return [0.0, []]
    [min_right, sorted_by_y_right] = minimum_distance_analyze(right)
    if min_right == 0.0:
        return [0.0, []]
    min = min_left if min_left < min_right else min_right

    ref_x = sorted_by_x[mid].x
    ref_x_left = ref_x - min
    ref_x_right = ref_x + min

    sorted_by_y = [0] * (len(sorted_by_y_left) + len(sorted_by_y_right))
    i = 0
    r = 0
    l = 0
    while True:
        cmp = sorted_by_y_left[l].y < sorted_by_y_right[r].y if sorted_by_y_left[l].y != sorted_by_y_right[r].y else sorted_by_y_left[l].x < sorted_by_y_right[r].x
        if cmp:
            sorted_by_y[i] = sorted_by_y_left[l]
            i += 1
            l += 1
            if l == len(sorted_by_y_left):
                sorted_by_y[i:] = sorted_by_y_right[r:]
                break
        else:
            sorted_by_y[i] = sorted_by_y_right[r]
            i += 1
            r += 1
            if r == len(sorted_by_y_right):
                sorted_by_y[i:] = sorted_by_y_left[l:]
                break

    candidates = []
    for p in sorted_by_y:
        if p.x > ref_x_left and p.x < ref_x_right:
            candidates.append(p)
    
    for a_idx, a in enumerate(candidates):
        for b in candidates[a_idx+1:a_idx+9]:
            if abs(a.y-b.y) < min:
                d = dist(a, b)
                if d < min:
                    min = d

    return [min, sorted_by_y]

def minimum_distance_fast(x, y):
    points_list = [Point(x[i], y[i]) for i in range(len(x))]

    sorted_by_x = sort(points_list)

    [min, sorted_by_y] = minimum_distance_analyze(sorted_by_x)

    return min

def minimum_distance_naive(x, y):
    min = float('Inf')
    for a in range(len(x)):
        for b in range(len(x)):
            if a != b:
                dist = math.pow(x[a]-x[b], 2) + math.pow(y[a]-y[b], 2)
                if dist < min:
                    min = dist
    return math.sqrt(min)

def test(input):
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    return minimum_distance_fast(x, y)

def unit_test():
    tests = [\
        ["2\n0 0\n3 4", 5.0],
        ["4\n7 7\n1 100\n4 8\n7 7", 0.0],
        ["11\n4 4\n-2 -2\n-3 -4\n-1 3\n2 3\n-4 0\n1 1\n-1 -1\n3 -1\n-4 2\n-2 4", 1.4142135623730951]]

    for t in tests:
        res = test(t[0])
        print(res)
        print(t[1])
        print("passed" if res == t[1] else "failed")

def live():
    res = test(sys.stdin.read())
    print("{0:.9f}".format(res))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:
        live()
