#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operators = "+-*/"
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if op == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
        sys.exit(0)
    if op == '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        sys.exit(0)
    if op == '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        sys.exit(0)
    if op == '/':
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
        sys.exit(0)
