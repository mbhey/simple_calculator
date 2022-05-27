#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_calculator.main import SimpleCalculator
import pytest


def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5)

    assert result == 9


def test_add_multiple_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(5, 6, 7, 8, 9)

    assert result == 35


def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.subtract(5, 4)

    assert result == 1


def test_subtract_numbers():
    calculator = SimpleCalculator()
    result = calculator.subtract(100, 50, 25, 15, 5)

    assert result == 5


def test_multiply_many_numbers():
    numbers = range(1, 10)

    calculator = SimpleCalculator()

    result = calculator.multiply(*numbers)

    assert result == 362880


def test_multiply_by_zero():
    calculator = SimpleCalculator()
    with pytest.raises(ValueError):
        result = calculator.multiply(10, 5, 0)
        assert result == 0


def test_devision():
    calculator = SimpleCalculator()
    result = calculator.divide(10, 2)
    assert result == 5.0


def test_devide_by_zero():
    calculator = SimpleCalculator()

    result = calculator.divide(10, 0)

    assert result == float("inf")
