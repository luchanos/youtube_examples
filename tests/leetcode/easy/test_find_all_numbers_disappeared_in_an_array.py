"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

from typing import List
import pytest


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mapper = {x: 0 for x in range(1, n + 1)}
        for el in nums:
            mapper[el] += 1
        return [x for x in mapper if mapper[x] == 0]


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [4, 3, 2, 7, 8, 2, 3, 1]}, [5, 6]),
    ({"nums": [1, 1]}, [2])
])
def test_remove_element(input_data, expected):
    sol = Solution()
    assert sol.findDisappearedNumbers(**input_data) == expected
