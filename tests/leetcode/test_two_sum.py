"""
https://leetcode.com/problems/two-sum/
"""
from typing import List
import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            pre_target = target - nums[i]
            for j in range(1, len(nums)):
                if i != j and nums[j] == pre_target:
                    return [i, j]


s = Solution()


@pytest.mark.parametrize("nums, target, expected", [
    ([0, 1, 2, 3, 4], 7, [3, 4]),
    ([3, 2, 4], 6, [1, 2]),
    ([2, 5, 5, 11], 10, [1, 2]),
    ([-3, 4, 3, 90], 0, [0, 2])
])
def test_two_sum(nums, target, expected):
    assert s.twoSum(nums, target) == expected
