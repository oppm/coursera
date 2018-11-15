# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
        elif a[i] < x:
            k += 1
            a[i], a[k] = a[k], a[i]
            j += 1
            a[k], a[j] = a[j], a[k]
    a[l], a[j] = a[j], a[l]        
    return j, k    

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = "5\n2 3 9 2 2"
    input = "8\n1 5 1 2 2 8 1 9"
    input = "8\n1 2 3 4 5 6 7 8"
    input = "8\n8 7 6 5 4 3 2 1"
    input = "8\n4 7 4 7 4 7 4 7"
    input = "5\n2 3 9 2 9"
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
