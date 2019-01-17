# python3
import sys
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, next in enumerate(text):
        if next in "([{":
            stack.append([i, next])

        if next in ")]}":
            if len(stack) > 0:
                [opening_i, opening] = stack.pop()
                if (next == ")" and opening in "[{") or \
                    (next == "]" and opening in "({") or \
                    (next == "}" and opening in "(["):

                    return str(i+1)
            else:
                return str(i+1)

    if len(stack) > 0:
        [opening_i, opening] = stack[0]
        return str(opening_i+1)

    return "Success" 


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

def test(s, res):
    print("passed" if find_mismatch(s) == res else "failed")

def unit_test():
    test("[]", "Success")
    test("{}[]", "Success")
    test("[({})]", "Success")
    test("{()}[]", "Success")
    test("{", "1")
    test("{[}", "3")    
    test("foo(bar);", "Success")
    test("foo(bar[i);", "10")
    test("foo(bar[i];", "4")
    test("}", "1")
    test("foo}", "4")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        unit_test()
    else:
        main()
