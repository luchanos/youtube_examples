"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""

import pytest
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m * n != len(original):
            return res
        else:
            cnt = 0
            for i in range(m):
                new_str = []
                for j in range(n):
                    new_str.append(original[cnt])
                    cnt += 1
                res.append(new_str)
        return res


@pytest.mark.parametrize("input_data, expected", [
    ({"original": [1, 2, 3, 4], "m": 2, "n": 2}, [[1, 2], [3, 4]]),
    ({"original": [1, 2, 3], "m": 1, "n": 3}, [[1, 2, 3]]),
    ({"original": [1, 2], "m": 1, "n": 1}, [])
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.construct2DArray(**input_data) == expected
