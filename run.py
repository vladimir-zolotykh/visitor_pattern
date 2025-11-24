#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
class Node:
    pass


class Number(Node):
    def __init__(self, val):
        self.number = val


class BinOp(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinOp):
    pass


class Mul(BinOp):
    pass


class Visitor:
    def visit(node: Node):
        pass


class Evaluator:
    pass


class Printer:
    pass


def run_test():
    """
    >>> True
    True
    """
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    expr = Add(Number(3), Mul(Number(4), Number(5)))
