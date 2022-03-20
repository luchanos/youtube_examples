"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""

import pytest
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapper = {}
        for num in nums:
            if num not in mapper:
                mapper[num] = 1
            else:
                mapper[num] += 1
        return [x for x in mapper if mapper[x] > 1]


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [4, 3, 2, 7, 8, 2, 3, 1]}, [2, 3]),
    ({"nums": [1, 1, 2]}, [1]),
    ({"nums": [1]}, []),
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.findDuplicates(**input_data) == expected
