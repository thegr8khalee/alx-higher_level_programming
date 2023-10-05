#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    i = 10
    x = 5

    print("{} + {}".format(i, x, add(i, x)))
    print("{} + {}".format(i, x, sub(i, x)))
    print("{} + {}".format(i, x, mul(i, x)))
    print("{} + {}".format(i, x, div(i, x)))
