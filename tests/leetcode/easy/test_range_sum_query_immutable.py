"""
https://leetcode.com/problems/range-sum-query-immutable/
"""

from typing import List
import pytest


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [-2, 0, 3, -5, 2, -1], "ranges": [0, 2]}, 1),
    ({"nums": [-2, 0, 3, -5, 2, -1], "ranges": [2, 5]}, -1),
    ({"nums": [-2, 0, 3, -5, 2, -1], "ranges": [0, 5]}, -3),
])
def test_single_number(input_data, expected):
    sol = NumArray(input_data["nums"])
    assert sol.sumRange(input_data["ranges"][0], input_data["ranges"][1]) == expected
