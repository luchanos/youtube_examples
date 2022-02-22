"""
https://leetcode.com/problems/length-of-last-word/
"""

import pytest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


@pytest.mark.parametrize("s, expected", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6)
])
def test_remove_element(s, expected):
    sol = Solution()
    assert sol.lengthOfLastWord(s) == expected
