"""
https://leetcode.com/problems/two-sum/
"""

from typing import List
import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [2, 7, 11, 15], "target": 9}, [0, 1]),
    ({"nums": [3, 2, 4], "target": 6}, [1, 2]),
    ({"nums": [3, 3], "target": 6}, [0, 1])
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.twoSum(**input_data) == expected
