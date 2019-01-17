#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = []
        self._max = 0

    def Push(self, a):
        self._max = max(self._max, a)
        self.__stack.append(a)
        self.__max.append(self._max)

    def Pop(self):
        assert(len(self.__stack) > 0)
        self.__stack.pop()
        self.__max.pop()
        self._max = self.__max[len(self.__max)-1]

    def Max(self):
        assert(len(self.__stack) > 0)
        return self._max

def test():
    stack = StackWithMax()
    stack.Push(2)
    assert(stack._max == 2)
    stack.Push(3)
    assert(stack._max == 3)
    stack.Push(55)
    assert(stack._max == 55)
    stack.Pop()
    assert(stack._max == 3)
    stack.Push(22)
    assert(stack._max == 22)
    stack.Pop()
    assert(stack._max == 3)
    stack.Pop()
    assert(stack._max == 2)

def main():
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()