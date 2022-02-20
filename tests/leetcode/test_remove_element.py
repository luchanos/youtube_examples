"""
https://leetcode.com/problems/remove-element/
"""

import pytest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        while True:
            if len(nums) == cnt:
                break
            elif len(nums) == 0:
                return 0
            elif nums[cnt] == val:
                nums.pop(cnt)
                continue
            cnt += 1
        return len(nums)


@pytest.mark.parametrize("input_value, val, expected", [
    ([1, 1, 2, 2, 2, 3, 3, 4], 1, 6),
    ([], 1, 0),
    ([1, ], 1, 0),
    ([1, 2, 3, 4], 0, 4),
    ([3, 2, 2, 3], 3, 2)
])
def test_remove_element(input_value, val, expected):
    sol = Solution()
    assert sol.removeElement(input_value, val) == expected
