# Uses python3
import sys

def binary_search_range(a, left, right, x):

    if left > right:
        return -1

    mid = int((right+left)/2)

    if a[mid] > x:
        return binary_search_range(a, left, mid-1, x)
    elif a[mid] < x:
        return binary_search_range(a, mid+1, right, x)
    else:
        return mid

def binary_search(a, x):
    left, right = 0, len(a)

    return binary_search_range(a, left, right-1, x)    

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = "5 1 5 8 12 13\n6 8 1 23 1 12 0"
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
