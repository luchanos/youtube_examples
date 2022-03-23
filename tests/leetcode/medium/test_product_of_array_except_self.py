"""
https://leetcode.com/problems/product-of-array-except-self/
"""

import pytest
from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeros_cnt = nums.count(0)
        if zeros_cnt > 1:
            return [0 for _ in range(len(nums))]
        if zeros_cnt == 0:
            total_mul = reduce(lambda x, y: x * y, nums)
            for n in nums:
                res.append(int(total_mul / n))
            return res
        if zeros_cnt == 1:
            total_mul = 1
            for el in nums:
                total_mul *= el if el != 0 else 1
            for n in nums:
                res.append(0 if n != 0 else total_mul)
            return res


@pytest.mark.parametrize("input_data, expected", [
    ({"nums": [-1, 1, 0, -3, 3]}, [0, 0, 9, 0, 0]),
    ({"nums": [1, 2, 3, 4]}, [24, 12, 8, 6]),
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.productExceptSelf(**input_data) == expected
