"""
https://leetcode.com/problems/palindrome-linked-list/
"""
from typing import Optional
import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        cur = head
        while True:
            values.append(cur.val)
            if cur.next is None:
                break
            cur = cur.next
        return values == values[::-1]


@pytest.mark.parametrize("input_data, expected", [
    ({"head": ListNode(1, ListNode(2, ListNode(2, ListNode(1))))}, True),
    ({"head": ListNode(1, ListNode(2))}, False),
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.isPalindrome(**input_data) == expected
