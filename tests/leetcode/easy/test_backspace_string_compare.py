"""
https://leetcode.com/problems/backspace-string-compare/
"""

import pytest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_l = [[s, ""], [t, ""]]
        for l in res_l:
            for sym in l[0]:
                if sym == "#":
                    l[1] = l[1][:-1]
                    continue
                l[1] += sym
        return res_l[0][1] == res_l[1][1]


@pytest.mark.parametrize("input_data, expected", [
    ({"s": "a#c", "t": "b"}, False),
    ({"s": "ab#c", "t": "ad#c"}, True),
    ({"s": "ab##", "t": "c#d#"}, True)
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.backspaceCompare(**input_data) == expected
