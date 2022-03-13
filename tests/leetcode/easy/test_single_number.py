"""
https://leetcode.com/problems/single-number/
"""

from typing import List
import pytest
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [2, 2, 1]}, 1),
    ({"nums": [4, 1, 2, 1, 2]}, 4),
    ({"nums": [1]}, 1)
])
def test_single_number(input_data, expected):
    sol = Solution()
    assert sol.singleNumber(**input_data) == expected
