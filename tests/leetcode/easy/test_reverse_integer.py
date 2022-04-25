"""
https://leetcode.com/problems/reverse-integer/
"""

import pytest


class Solution:
    def reverse(self, x: int) -> int:
        res = -int(str(x)[:0:-1]) if x < 0 else int(str(x)[::-1])
        return res if -2147483648 <= res < 2147483648 else 0


@pytest.mark.parametrize("input_value, expected", [(123, 321),
                                                   (-123, -321),
                                                   (120, 21),
                                                   (0, 0),
                                                   (1534236469, 0)])
def test_reverse(input_value, expected):
    sol = Solution()
    assert sol.reverse(input_value) == expected
