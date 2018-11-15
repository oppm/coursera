# Uses python3
import sys

def optimal_summands(candies):
    summands = []
    price = 1
    while candies > 0:
        diff = candies - price
        if diff <= price:
            price = candies

        summands.append(price)
        candies -= price
        price += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
