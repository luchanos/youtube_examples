"""
https://leetcode.com/problems/valid-palindrome/
"""

import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join([x for x in s if 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122 or 48 <= ord(x) <= 57])
        return s1.lower() == s1.lower()[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        cnt_forward = 0
        cnt_backward = len(s) - 1
        while True:
            if cnt_forward == len(s):
                break
            if not (
                    65 <= ord(s[cnt_forward]) <= 90 or
                    97 <= ord(s[cnt_forward]) <= 122 or
                    48 <= ord(s[cnt_forward]) <= 57
            ):
                cnt_forward += 1
                continue
            if not (
                    65 <= ord(s[cnt_backward]) <= 90 or
                    97 <= ord(s[cnt_backward]) <= 122 or
                    48 <= ord(s[cnt_backward]) <= 57
            ):
                cnt_backward -= 1
                continue
            if cnt_forward == cnt_backward:
                break
            if s[cnt_forward].lower() != s[cnt_backward].lower():
                return False
            cnt_forward += 1
            cnt_backward -= 1
        return True


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("a", True),
    ("a.", True),
    ("0P", False),
    ("..ab", False),
    ("ab_a", True)
])
def test_remove_element(s, expected):
    sol = Solution()
    assert sol.isPalindrome(s) is expected
