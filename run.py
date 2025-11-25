#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Literal
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
    pass


class Sub(BinOp):
    pass


class Mul(BinOp):
    pass


AddNode = Add
SubNode = Sub
MulNode = Mul
NumNode = Num


class Walker:
    def __init__(self, mode: Literal["eval", "print"] = "eval"):
        if mode not in ("eval", "print"):
            raise TypeError("Mode must be eval or print")
        self.mode = mode

    @singledispatchmethod
    def visit(self, node):
        raise NotImplementedError(f"No visit method for {type(node)}")

    @visit.register
    def _(self, node: AddNode):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return (
            left + right if self.mode == "eval" else "{:s} + {:s}".format(left, right)
        )

    @visit.register
    def _(self, node: SubNode):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return (
            left - right if self.mode == "eval" else "{:s} - {:s}".format(left, right)
        )

    @visit.register
    def _(self, node: MulNode):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return (
            left * right if self.mode == "eval" else "{:s} * {:s}".format(left, right)
        )

    @visit.register
    def _(self, node: NumNode):
        return node.val if self.mode == "eval" else str(node.val)


def run_test():
    """
    >>> expr = Add(Num(3), Mul(Num(4), Num(5)))
    >>> evaluator = Walker("eval")
    >>> evaluator.visit(expr)
    23
    >>> printer = Walker("print")
    >>> printer.visit(expr)
    '3 + 4 * 5'
    """
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    run_test()
