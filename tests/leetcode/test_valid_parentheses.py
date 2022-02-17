"""
https://leetcode.com/problems/valid-parentheses/
"""

import pytest


class Solution:
    MAPPER = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for el in s:
            if el in self.MAPPER:
                stack.append(el)
                continue
            if len(stack) != 0 and el == self.MAPPER[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack) != 0:
            return False
        return True


@pytest.mark.parametrize("input_value, expected", [
                                                   ("()", True),
                                                   ("()[]{}", True),
                                                   ("(]", False),
                                                   ("[", False),
                                                   ("((", False),
                                                   ("){", False)])
def test_is_valid(input_value, expected):
    sol = Solution()
    assert sol.isValid(input_value) is expected
