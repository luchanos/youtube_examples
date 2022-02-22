"""
https://leetcode.com/problems/merge-sorted-array/
"""

from typing import List
import pytest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        return nums1


@pytest.mark.parametrize("nums1, m, nums2, n, expected", [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1])
])
def test_remove_element(nums1, m, nums2, n, expected):
    sol = Solution()
    assert sol.merge(nums1, m, nums2, n) == expected
