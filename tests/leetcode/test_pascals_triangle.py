"""
https://leetcode.com/problems/pascals-triangle/
"""

import pytest
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            prev_row = [1, 1]
            for i in range(numRows - 2):
                next_row = [prev_row[0]]
                cnt = 0
                while True:
                    next_row.append(prev_row[cnt] + prev_row[cnt + 1])
                    cnt += 1
                    if cnt == len(prev_row) - 1:
                        break
                next_row.append(prev_row[-1])
                res.append(next_row)
                prev_row = next_row
            return res


@pytest.mark.parametrize("input_value, expected", [(5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
                                                   (1, [[1]])])
def test_generate(input_value, expected):
    sol = Solution()
    assert sol.generate(input_value) == expected
