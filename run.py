#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
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


class Mul(BinOp):
    pass


class Visitor:
    def visit(self, node: Node):
        name = f"visit_{type(node).__name}"
        method = getattr(self, name, self.visit_generic)
        return method(node)

    def visit_generic(self, node: Node):
        raise TypeError(f"Don't know how to visit {node}")


class Evaluator(Visitor):
    def visit_Add(self, node: Node) -> float:
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node: Node) -> float:
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node: Node) -> float:
        return self.visit(node.left) * self.visit(node.right)

    def visit_Num(self, node: Node) -> float:
        return node.val


class Printer:
    def visit_Add(self, node: Node) -> str:
        return "{:s} + {:s}".format(self.visit(node.left), self.visit(node.right))

    def visit_Sub(self, node: Node):
        return "{:s} - {:s}".format(self.visit(node.left), self.visit(node.right))

    def visit_Mul(self, node: Node):
        return "{:s} * {:s}".format(self.visit(node.left), self.visit(node.right))

    def visit_Num(self, node: Node) -> str:
        return str(node.val)


def run_test():
    """
    >>> True
    True
    """
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    expr = Add(Num(3), Mul(Num(4), Num(5)))
    evaluator = Evaluator()
    print(evaluator.visit(expr))
    printer = Printer()
    print(printer.visit(expr))
