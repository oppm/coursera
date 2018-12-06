# Uses python3
import sys

class Point:
    def __init__(self, t, x, cnt_idx=0):
        self.t = t
        self.x = x
        self.cnt_idx = cnt_idx


def my_merge_sort(unsorted):
    
    if len(unsorted) <= 1:
        return unsorted

    mid = len(unsorted)//2

    left = my_merge_sort(unsorted[:mid])
    right = my_merge_sort(unsorted[mid:])

    points = [0] * len(unsorted)
    i = 0
    l = 0
    r = 0
    while True:
        cmp_res = (left[l].x < right[r].x) if (left[l].x != right[r].x) else (left[l].t < right[r].t)

        if cmp_res:
            points[i] = left[l]
            i += 1
            l += 1
            if l == len(left): # Done with left side. Copy rest of right side
                points[i:] = right[r:]
                break
        else:
            points[i] = right[r]
            i += 1
            r += 1
            if r == len(right):
                points[i:] = left[l:]
                break        

    return points

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    unsorted_points = []
    unsorted_points.extend([Point(0, point) for point in starts])
    unsorted_points.extend([Point(1, point, point_i) for point_i, point in enumerate(points)])
    unsorted_points.extend([Point(2, point) for point in ends])
    
    sorted_points = my_merge_sort(unsorted_points)

    overlap = 0
    for p in sorted_points:
        if p.t == 0: # start point
            overlap += 1
        elif p.t == 1: # selected point
            cnt[p.cnt_idx] = overlap
        else: # end point
            overlap -= 1

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

def test(input):
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    return fast_count_segments(starts, ends, points)

def unit_test():
    tests = [\
        ["2 3\n0 5\n7 10\n1 6 11", [1, 0, 0]],
        ["1 3\n-10 10\n-100 100 0", [0, 0, 1]],
        ["3 2\n0 5\n-3 2\n7 10\n1 6", [2, 0]]]

    for t in tests:
        res = test(t[0])
        print(t[0])
        print(res)
        print(t[1])
        print(">> passed" if res == t[1] else ">> failed")

def live():
    cnt = test(sys.stdin.read())
    for x in cnt:
        print(x, end=' ')

if __name__ == '__main__':
    live()