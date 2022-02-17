"""
https://leetcode.com/problems/longest-common-prefix/
"""

import pytest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        min_str_len = min([len(x) for x in strs])
        for i in range(min_str_len):
            if len(set([x[i] for x in strs])) == 1:
                result += strs[0][i]
            else:
                break
        return result


@pytest.mark.parametrize("input_value, expected", [(["flower", "flow", "flight"], "fl"),
                                                   (["dog", "racecar", "car"], ""),
                                                   (["cir", "car"], "c")])
def test_palidrome(input_value, expected):
    sol = Solution()
    assert sol.longestCommonPrefix(input_value) == expected
