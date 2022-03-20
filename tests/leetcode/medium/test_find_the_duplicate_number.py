"""
https://leetcode.com/problems/find-the-duplicate-number/
"""

import pytest
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapper = {}
        for el in nums:
            if el not in mapper:
                mapper[el] = 1
            else:
                return el


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [1, 3, 4, 2, 2]}, 2),
    ({"nums": [3, 1, 3, 4, 2]}, 3),
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.findDuplicate(**input_data) == expected
