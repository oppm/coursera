# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:        
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))                
                self.depth = [0] * self.n

        def force(self, n, s):
                self.n = int(n)
                self.parent = list(map(int, s.split()))
                self.depth = [0] * self.n

        def get_depth(self, node):
                if self.depth[node] > 0:
                        return self.depth[node]

                parent = self.parent[node]
                depth = 1
                if parent != -1:
                        depth = 1 + self.get_depth(parent)
                self.depth[node] = depth
                return depth

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for node in range(self.n):
                        depth = self.get_depth(node)
                        maxHeight = max(maxHeight, depth)
                return maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())


def test(n, s, o):
        tree = TreeHeight()
        tree.force(n, s)
        print("passed" if tree.compute_height() == o else "failed" )

def unit_test():
        test(5, "4 -1 4 1 1", 3)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        unit_test()
    else:
        threading.Thread(target=main).start()
