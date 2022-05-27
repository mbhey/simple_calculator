# -*- coding: utf-8 -*-
from decimal import DivisionByZero
from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        result = 0
        for num in args:
            result = result + num
        return result

    def subtract(self, *args):
        result = args[0]
        for num in range(1, len(args)):
            result = result - args[num]
        return result

    def multiply(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def divide(self, numerator, denominator):
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return float("inf")
