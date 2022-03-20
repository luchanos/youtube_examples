"""
https://leetcode.com/problems/squares-of-a-sorted-array/
"""

from typing import List
import pytest


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x * x for x in nums])


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [-4, -1, 0, 3, 10]}, [0, 1, 9, 16, 100]),
    ({"nums": [-7, -3, 2, 3, 11]}, [4, 9, 9, 49, 121])
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.sortedSquares(**input_data) == expected
