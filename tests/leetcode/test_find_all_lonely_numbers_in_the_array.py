"""
https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/submissions/
"""

import pytest
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums

        res = []
        nums.sort()
        cnt = 0

        while True:
            if cnt == len(nums) - 1:
                if nums[cnt] not in {nums[cnt - 1] + 1, nums[cnt - 1]}:
                    res.append(nums[cnt])
                break
            if nums[cnt] in {nums[cnt + 1], nums[cnt - 1]}:
                cnt += 1
                continue
            if nums[cnt] == nums[cnt - 1] + 1:
                cnt += 1
                continue
            if nums[cnt] == nums[cnt + 1] - 1:
                cnt += 1
                continue
            res.append(nums[cnt])
            cnt += 1
        return res


@pytest.mark.parametrize("input_value, expected", [([69, 45, 69], [45]),
                                                   ([1, 3, 5, 3], [1, 5]),
                                                   ([10, 6, 5, 8], [10, 8]),

                         ])
def test_find_lonely(input_value, expected):
    sol = Solution()
    assert sol.findLonely(input_value) == expected
