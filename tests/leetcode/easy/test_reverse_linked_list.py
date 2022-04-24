"""
https://leetcode.com/problems/reverse-linked-list/submissions/
"""

from typing import List, Optional
import pytest

from tests.leetcode.easy.utils import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        stack_vals = []
        current_node = head
        while True:
            stack_vals.append(current_node.val)
            if current_node.next is None:
                break
            current_node = current_node.next

        prev_node = None
        node = None
        for i in range(len(stack_vals)):
            node = ListNode(stack_vals[i])
            if prev_node is None:
                prev_node = node
                continue
            node.next = prev_node
            prev_node = node
        return node


@pytest.mark.parametrize("input_data, expected", [
    ({"head": ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))},
     ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))),
])
def test_search(input_data, expected):
    sol = Solution()
    assert sol.reverseList(**input_data) == expected
