from itertools import count
import pytest


def get_number_of_squares(n):
    res = 0
    cnt = 0
    cnt_gen = count(1)
    while True:
        a = next(cnt_gen)
        if res + a ** 2 >= n:
            return cnt
        res += a ** 2
        cnt += 1


@pytest.mark.parametrize("n, expected", ((1, 0),
                                         (2, 1),
                                         (5, 1),
                                         (6, 2),
                                         (15, 3),))
def test_get_number_of_squares(n, expected):
    assert get_number_of_squares(n) == expected
