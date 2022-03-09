"""
https://leetcode.com/problems/a-number-after-a-double-reversal/
"""

import pytest


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return int(str(num)[::-1].strip("0")[::-1]) == num


@pytest.mark.parametrize("input_data, expected", [
    (526, True),
    (1800, False),
    (0, True)
])
def test_remove_element(input_data, expected):
    sol = Solution()
    assert sol.isSameAfterReversals(input_data) == expected
