#!/usr/bin/env python3
"""Tests for Scientific Calculator"""

import sys
sys.path.insert(0, '.')
from calculator import Calculator

def test_basic():
    calc = Calculator()
    assert calc.calculate('+', 2, 3) == 5
    assert calc.calculate('-', 10, 4) == 6
    assert calc.calculate('*', 3, 4) == 12
    assert calc.calculate('/', 10, 2) == 5

def test_scientific():
    calc = Calculator()
    assert abs(calc.calculate('sqrt', 16) - 4) < 0.001
    assert calc.calculate('factorial', 5) == 120

if __name__ == "__main__":
    test_basic()
    test_scientific()
    print("All tests passed!")
