"""
https://leetcode.com/problems/middle-of-the-linked-list/
"""

from typing import Optional
import pytest

from tests.leetcode.easy.utils import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        len_l = 1
        cur = head
        mapper = {}
        while True:
            mapper[len_l] = cur
            if cur.next is None:
                break
            len_l += 1
            cur = cur.next
        if len_l == 1:
            return head
        mid = len_l // 2 + len_l % 2 + 1 * (1 if len_l % 2 == 0 else 0)
        return mapper[mid]


@pytest.mark.parametrize("input_data, expected", [
    ({"head": ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))},
     ListNode(3, ListNode(4, ListNode(5))))
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.middleNode(**input_data) == expected
