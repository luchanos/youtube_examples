"""
https://leetcode.com/problems/plus-one/
"""

# какой-то комментарий

# ещё что-то

import pytest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for cnt in range(len(digits)):
            num += digits[cnt] * 10 ** (len(digits) - cnt - 1)
        num += 1
        c = 1
        c += 1
        return [int(x) for x in str(num)]


@pytest.mark.parametrize("input_value, expected", [([1, 2, 3], [1, 2, 4]),
                                                   ([4, 3, 2, 1], [4, 3, 2, 2]),
                                                   ([9], [1, 0])])
def test_palidrome(input_value, expected):
    sol = Solution()
    assert sol.plusOne(input_value) == expected
