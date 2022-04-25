"""
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
"""
import pytest


def century(year):
    return year // 100 + 1 * (0 if year % 100 == 0 else 1)


@pytest.mark.parametrize("year, expected", [(1705, 18),
                                            (1900, 19)])
def test_solution(year, expected):
    assert century(year) == expected
