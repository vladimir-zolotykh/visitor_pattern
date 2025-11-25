#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from functools import singledispatchmethod


class Node:
    pass


class Num(Node):
    def __init__(self, val):
        self.val = val


class BinOp(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinOp):
    def __call__(self, left, right):
        return left + right


class Sub(BinOp):
    def __call__(self, left, right):
        return left - right


class Mul(BinOp):
    def __call__(self, left, right):
        return left * right


AddNode = Add
SubNode = Sub
MulNode = Mul
NumNode = Num


class Evaluator:
    def __init__(self, mode="eval"):
        self.mode = mode

    @singledispatchmethod
    def visit(self, node):
        raise NotImplementedError(f"No visit method for {type(node)}")

    @visit.register
    def _(self, node: AddNode) -> float:
        return node(self.visit(node.left), self.visit(node.right))

    @visit.register
    def _(self, node: SubNode) -> float:
        return node(self.visit(node.left), self.visit(node.right))

    @visit.register
    def _(self, node: MulNode) -> float:
        return node(self.visit(node.left), self.visit(node.right))

    @visit.register
    def _(self, node: NumNode) -> float:
        return node.val


class Printer:
    @singledispatchmethod
    def visit(self, node) -> str:
        raise NotImplementedError(f"No visit method for {type(node)}")

    @visit.register
    def _(self, node: AddNode) -> str:
        return "{:s} + {:s}".format(self.visit(node.left), self.visit(node.right))

    @visit.register
    def _(self, node: SubNode) -> str:
        return "{:s} - {:s}".format(self.visit(node.left), self.visit(node.right))

    @visit.register
    def _(self, node: MulNode) -> str:
        return "{:s} * {:s}".format(self.visit(node.left), self.visit(node.right))

    @visit.register
    def _(self, node: NumNode) -> str:
        return str(node.val)


def run_test():
    """
    >>> expr = Add(Num(3), Mul(Num(4), Num(5)))
    >>> evaluator = Evaluator()
    >>> evaluator.visit(expr)
    23
    >>> printer = Printer()
    >>> printer.visit(expr)
    '3 + 4 * 5'
    """
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    run_test()
