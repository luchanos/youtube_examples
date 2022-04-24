"""
https://leetcode.com/problems/remove-linked-list-elements/submissions/
"""
from typing import Optional
import pytest

from tests.leetcode.easy.utils import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cur = head

        if head is None:
            return

        if head.next is None:
            return head

        while cur is not None:
            if cur.val not in values:
                values.append(cur.val)
            cur = cur.next

        result = None
        if len(values) == 0:
            return
        if len(values) == 1:
            return ListNode(values[0])

        is_next = ListNode(values[-1])
        for val in values[-2::-1]:
            result = ListNode(val, is_next)
            is_next = result
        return result


@pytest.mark.parametrize("input_data, expected", [
    ({"head": ListNode(-1, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(3, ListNode(3)))))))},
     ListNode(-1, ListNode(0, ListNode(3)))),
    ({"head": ListNode(1, ListNode(1, ListNode(2)))}, ListNode(1, ListNode(2))),
    ({"head": ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, )))))},
     ListNode(1, ListNode(2, ListNode(3)))),
    ({"head": ListNode(1, ListNode(1, ListNode(2)))}, ListNode(1, ListNode(2)))
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.deleteDuplicates(**input_data) == expected
