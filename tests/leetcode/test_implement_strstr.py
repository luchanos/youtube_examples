"""
https://leetcode.com/problems/implement-strstr/
"""

import pytest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)


@pytest.mark.parametrize("haystack, needle, expected", [
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("", "", 0),
])
def test_remove_element(haystack, needle, expected):
    sol = Solution()
    assert sol.strStr(haystack, needle) == expected
