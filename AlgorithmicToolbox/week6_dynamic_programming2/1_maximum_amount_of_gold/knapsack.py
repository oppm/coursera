# Uses python3
import sys

def optimal_weight_greedy(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight(W, w):
    
    m = [[0] * (W+1) for _ in range(len(w)+1)]

    for i in range(len(w)):
        item_weight = w[i]
        for c in range(1, W+1):
            weight_not_taken = m[i][c]
            highest_weight = weight_not_taken

            if c >= item_weight:
                weight_if_taken = m[i][c-item_weight] + item_weight
                if weight_if_taken > weight_not_taken:
                    highest_weight = weight_if_taken
            
            m[i+1][c] = highest_weight

    return m[len(w)][W]


def test(W, w, res):
    print("passed" if optimal_weight(W, w) == res else "failed")

def unit_test():
    test(10, [1,4,8], 9)
    test(20, [5, 7, 12, 18], 19)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:        
        input = sys.stdin.read()
        W, n, *w = list(map(int, input.split()))
        print(optimal_weight(W, w))
