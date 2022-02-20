"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array
"""

import pytest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) in {0, 1}:
            return len(nums)
        prev = nums[0]
        cnt = 1
        while True:
            if nums[cnt] != prev:
                prev = nums[cnt]
                cnt += 1
            else:
                nums.pop(cnt)
            if cnt == len(nums):
                break
        return len(nums)


@pytest.mark.parametrize("input_value, expected", [
    ([1, 1, 2, 2, 2, 3, 3, 4], [1, 2, 3, 4]),
    ([], []),
    ([1, ], [1, ]),
    ([1, 2, 3, 4], [1, 2, 3, 4])
])
def test_is_valid(input_value, expected):
    sol = Solution()
    assert sol.removeDuplicates(input_value) == expected
