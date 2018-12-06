# Uses python3
import sys

def greedy(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence(n):

    a = [n for i in range(3*n)]
    b = [0 for i in range(3*n)]

    a[0] = 0
    b[0] = 1
    for i in range(1, n):
        num_ops = a[i-1]+1        
        
        if a[i+1-1] > num_ops:
            a[i+1-1] = num_ops
            b[i+1-1] = i
        if a[i*2-1] > num_ops:
            a[i*2-1] = num_ops
            b[i*2-1] = i
        if a[i*3-1] > num_ops:
            a[i*3-1] = num_ops
            b[i*3-1] = i

    sequence = []
    i = n
    while i > 1:
        sequence.append(i)
        i = b[i-1]

    sequence.append(1)
    return reversed(sequence)

def test(n, k, a):
    seq = list(optimal_sequence(n))
    same_length = len(seq) == k+1
    same_content = seq == a
    print("passed" if same_length and same_content else "failed")

def unit_test():
    test(1, 0, [1])
    test(5, 3, [1, 2, 4, 5])
    test(96234, 14, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:    
        input = sys.stdin.read()
        n = int(input)
        sequence = list(optimal_sequence(n))
        print(len(sequence) - 1)
        for x in sequence:
            print(x, end=' ')
