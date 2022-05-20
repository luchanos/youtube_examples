"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""

import pytest
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


@pytest.mark.parametrize("input_data, expected", [
    ({"arr": [0, 1, 0]}, 1),
    ({"arr": [0, 2, 1, 0]}, 1),
    ({"arr": [0, 10, 5, 2]}, 1),
    ({"arr": [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]}, 2)
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.peakIndexInMountainArray(**input_data) == expected
