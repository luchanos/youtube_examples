"""
https://leetcode.com/problems/binary-search/
"""
#todo luchanos перерешать самостоятельно

from typing import List
import pytest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [-1, 0, 3, 5, 9, 12], "target": 10}, -1),
    ({"nums": [-1, 0, 3, 5, 9, 12], "target": 2}, -1),
    ({"nums": [-1, 0, 3, 5, 9, 12], "target": 9}, 4)
])
def test_search(input_data, expected):
    sol = Solution()
    assert sol.search(**input_data) == expected
