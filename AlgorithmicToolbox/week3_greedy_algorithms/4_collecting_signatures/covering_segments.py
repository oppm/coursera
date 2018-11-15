# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segment_valid = [True] * len(segments)
    while True:
        segment_found = False
        end_time = 10**10
        for i, s in enumerate(segments):
            # find earliest end time
            if s.end < end_time and segment_valid[i]:
                end_time = s.end
                segment_found = True
        if not segment_found:
            break

        points.append(end_time)

        for i, s in enumerate(segments):
            if s.start <= end_time and end_time <= s.end:
                segment_valid[i] = False


    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
