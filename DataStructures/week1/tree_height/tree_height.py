# python3

import sys
import threading


def get_depth(self, node):
    if self.depth[node] > 0:
        return self.depth[node]
            
    parent = self.parent[node]
    depth = 1
    if parent != -1:
        depth = 1 + self.get_depth(parent)
    self.depth[node] = depth
    return depth

def compute_height(self, n, parents):
    # Replace this code with a faster implementation
    maxHeight = 0
    for node in range(self.n):
        depth = self.get_depth(node)
        maxHeight = max(maxHeight, depth)
    return maxHeight

def test(n, s, o):
    parents = list(map(int, s.split()))
    print("passed" if tree.compute_height(n, parents) == o else "failed" )

def unit_test():
        test(5, "4 -1 4 1 1", 3)   

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
