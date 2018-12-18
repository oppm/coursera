# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        b[left] = a[left]
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    # calc number_of_inversions
    l = left
    r = ave
    while (l < ave) and (r < right):
        if a[r] < a[l]:
            number_of_inversions += (ave-l)
            r += 1
        else:
            l += 1

    # merge sort
    i = left
    l = left
    r = ave
    while True:
        left_done = (l == ave)
        right_done = (r == right)

        if right_done: 
            if left_done:
                break
            else:
                b[i:right] = a[l:ave]
                break
        else:
            if left_done:
                b[i:right] = a[r:right]
                break
            else:
                if a[r] < a[l]:
                    b[i] = a[r]
                    r += 1
                else:
                    b[i] = a[l]
                    l += 1
        i += 1

    a[left:right] = b[left:right]

    return number_of_inversions

if __name__ == '__main__':
    input = "5\n2 3 9 2 9"
    input = "5\n1 2 3 4 5"
    input = "5\n5 4 3 2 1"
    #input = "2\n5 4"
    #input = "3\n5 4 4"
    #input = "4\n5 4 4 4"
    #input = "3\n5 4 3"
    #input = "4\n5 4 3 2"    
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
    pass