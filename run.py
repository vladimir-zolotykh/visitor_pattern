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
    def __init__(self, left, right, op=None):
        self.left = left
        self.right = right
        self.op = op


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


# class Visitor:
#     def visit(self, node: Node) -> Any:
#         name = f"visit_{type(node).__name__}"
#         method = getattr(self, name, self.visit_generic)
#         return method(node)

#     def visit_generic(self, node: Node) -> NoReturn:
#         raise TypeError(f"Don't know how to visit {node}")


class Evaluator:
    @singledispatchmethod
    def visit(self, node):
        raise NotImplementedError(f"No visit method for {type(node)}")

    @visit.register
    def _(self, node: AddNode) -> float:
        return self.visit(node.left) + self.visit(node.right)

    @visit.register
    def _(self, node: SubNode) -> float:
        return self.visit(node.left) - self.visit(node.right)

    @visit.register
    def _(self, node: MulNode) -> float:
        return self.visit(node.left) * self.visit(node.right)

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
