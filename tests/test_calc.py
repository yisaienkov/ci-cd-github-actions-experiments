"""
Tests for the module calc.py
"""

from src import calc


def test_1():
    """
    Some test
    """
    assert calc.new_add(2, 3) == 5


def test_2():
    """
    Some test
    """
    assert calc.new_pow(2, 3) == 8


def test_3():
    """
    docstring
    """
    assert {"a": 1020, "b": 3040, "c": 5060} == calc.get_dict()
