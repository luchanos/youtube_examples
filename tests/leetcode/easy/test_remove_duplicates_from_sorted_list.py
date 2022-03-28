"""
https://leetcode.com/problems/remove-linked-list-elements/submissions/
"""
from typing import Optional
import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: "ListNode"):
        cur_self = self
        cur_other = other

        while True:
            if cur_self is None and cur_other is None:
                return True
            if cur_self is not None and cur_other is not None and cur_self.val == cur_other.val:
                cur_self = cur_self.next
                cur_other = cur_other.next
                continue
            return False


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
