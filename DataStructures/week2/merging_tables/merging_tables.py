# python3

import sys

def getParent(parent, i):
    
    j = parent[i]
    if i != j:
        j = getParent(parent, j)
        parent[i] = j

    return j

def merge(parent, destination, source, n_rows):
    realDestination, realSource = getParent(parent, destination), getParent(parent, source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    parent[source] = destination
    n_rows[source] += n_rows[destination]
    n_rows[destination] = 0

    return True

def calc(n, merge_queries, n_rows):
    parent = list(range(0, n))
    m = len(merge_queries)
    outp = []

    for i in range(m):
        [destination, source] = merge_queries[i]
        merge(parent, destination - 1, source - 1, n_rows)
        outp.append(max(n_rows))

    return outp

def compare(a, b):
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
    else:
        return False        

def test(n_tables, n_rows, merge_queries, exp_output):
    ans = calc(n_tables, merge_queries, n_rows)
    print("passed" if compare(ans, exp_output) else "failed")        

def unit_test():
    test(5, [1, 1, 1, 1, 1], [[3, 5], [2, 4], [1, 4], [5, 4], [5, 3]], [2, 2, 3, 5, 5])
    test(6, [10, 0, 5, 0, 3, 3], [[6, 6], [6, 5], [5, 4], [4, 3]], [10, 10, 10, 11])

def main():
    n, m = map(int, sys.stdin.readline().split())
    n_rows = list(map(int, sys.stdin.readline().split()))
    rank = [1] * n
    merge_queries = []
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        merge_queries.append([destination, source])

    ans = calc(n, merge_queries, n_rows)
    
    for i in range(m):
        print(ans[i])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:
        main()  