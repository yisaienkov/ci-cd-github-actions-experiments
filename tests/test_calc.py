from src import calc


def test_1():
    assert calc.add(2, 3) == 5


def test_2():
    assert calc.pow(2, 3) == 8