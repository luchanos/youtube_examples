"""
https://leetcode.com/problems/counting-bits/
"""

from typing import List
import pytest


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [str(bin(i)).count("1") for i in range(n + 1)]


@pytest.mark.parametrize("input_data, expected", [
    ({"n": 2}, [0, 1, 1]),
    ({"n": 5}, [0, 1, 1, 2, 1, 2])
])
def test_remove_element(input_data, expected):
    sol = Solution()
    assert sol.countBits(**input_data) == expected
