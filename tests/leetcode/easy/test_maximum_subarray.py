"""
https://leetcode.com/problems/maximum-subarray/
"""

import pytest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = None
        cnt_start = 0
        cnt_finish = 0
        sums = []
        while True:
            if cnt_finish == len(nums):
                break
            while True:
                if cnt_finish == len(nums) + 1:
                    break
                ex = nums[cnt_start:cnt_finish]
                if ex:
                    sums.append(sum(ex))
                cnt_finish += 1
            cnt_start += 1
            cnt_finish = cnt_start
            if sums:
                if max_val is None or max(sums) > max_val:
                    max_val = max(sums)
            sums = []
        return max_val


@pytest.mark.parametrize("input_value, expected", [([-1], -1),
                                                   ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
                                                   ([1], 1),
                                                   ([5, 4, -1, 7, 8], 23)],)
def test_max_subarray(input_value, expected):
    sol = Solution()
    assert sol.maxSubArray(input_value) == expected
