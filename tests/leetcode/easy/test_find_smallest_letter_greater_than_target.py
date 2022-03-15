"""
https://leetcode.com/problems/binary-search/
"""

from typing import List
import pytest


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for let in letters:
            if let > target:
                return let
        return letters[0]


@pytest.mark.parametrize("input_data, expected", [
    ({"letters": ["c", "f", "j"], "target": "a"}, "c"),
    ({"letters": ["c", "f", "j"], "target": "c"}, "f"),
    ({"letters": ["c", "f", "j"], "target": "d"}, "f"),
    ({"letters": ["c", "f", "j"], "target": "j"}, "c")
])
def test_search(input_data, expected):
    sol = Solution()
    assert sol.nextGreatestLetter(**input_data) == expected
