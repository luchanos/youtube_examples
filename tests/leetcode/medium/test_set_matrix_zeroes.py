"""
https://leetcode.com/problems/set-matrix-zeroes/
"""

import pytest
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_pos = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros_pos.append((i, j))
        for zeros in zeros_pos:
            matrix[zeros[0]] = [0 for _ in range(len(matrix[0]))]
            for k in range(len(matrix)):
                matrix[k][zeros[1]] = 0
        return matrix


@pytest.mark.parametrize("input_data, expected", [
    ({"matrix": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]}, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.setZeroes(**input_data) == expected
