# https://www.codewars.com/kata/583ebb9328a0c034490001ba/train/python
import pytest


def duplicate_elements(m, n):
    return bool(set(m).intersection(n))


@pytest.mark.parametrize("m, n, expected", (([1, 2, 3, 4, 5], [1, 6, 7, 8, 9], True),
                         ([9, 8, 7], [8, 1, 3], True)))
def test_duplicate_elements(m, n, expected):
    assert duplicate_elements(m, n) is expected
