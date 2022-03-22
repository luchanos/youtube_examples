"""
https://leetcode.com/problems/majority-element/
"""

import pytest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        half = len(nums) // 2
        mapper = {}
        cur = 0
        cur_val = None
        for n in nums:
            if n in mapper:
                mapper[n] += 1
                if mapper[n] > cur and mapper[n] >= half:
                    cur = mapper[n]
                    cur_val = n
            else:
                mapper[n] = 1
        return cur_val


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [8, 8, 7, 7, 7]}, 7),
    ({"nums": [3, 2, 3]}, 3),
    ({"nums": [2, 2, 1, 1, 1, 2, 2]}, 2),
    ({"nums": [1]}, 1),
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.majorityElement(**input_data) == expected
