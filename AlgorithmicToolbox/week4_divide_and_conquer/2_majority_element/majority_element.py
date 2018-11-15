# Uses python3
import sys

def count_elem(a, left, right, x):
    count = 0
    for i in range(left, right+1):
        if a[i] == x:
            count += 1
    return count

def get_majority_element(a, left, right):
    if left == right:
        # In case of single leaf, return the element itself as it is the major
        return a[left]
    if left + 1 == right:
        # In case of only two left, check whether they are equal
        if a[left] == a[right]:
            return a[left]
        else:
            return -1

    # Combine
    mid = int((right+left)/2)

    major_left = get_majority_element(a, left, mid)
    if major_left != -1:
        # We might have a solution. Check wheter major_left is still a major on this level
        count = count_elem(a, left, right, major_left)
        if count > (right-left+1)/2:
            return major_left
    
    major_right = get_majority_element(a, mid+1, right)
    if major_right != -1:
        count = count_elem(a, left, right, major_right)
        if count > (right-left+1)/2:
            return major_right

    return -1

if __name__ == '__main__':
    input = "5\n2 3 9 2 2"
    input = "4\n1 2 3 4"
    input = "4\n1 2 3 1"
    input = "8\n5 5 5 5 1 1 1 5"
    input = "10\n512766168 717383758 5 126144732 5 573799007 5 5 5 405079772"
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
