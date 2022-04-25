"""
https://leetcode.com/problems/search-insert-position/
"""
# todo luchanos написать через бинарный поиск

import pytest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        cnt = 0
        while True:
            if len(nums) < cnt + 1 or nums[cnt] == target:
                return cnt
            elif nums[cnt] < target:
                cnt += 1
            else:
                return cnt


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1], 2, 1)
])
def test_remove_element(nums, target, expected):
    sol = Solution()
    assert sol.searchInsert(nums, target) == expected
