"""
https://leetcode.com/problems/remove-linked-list-elements/submissions/
"""
from typing import Optional
import pytest

from tests.leetcode.easy.utils import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = []
        cur = head

        if not head:
            return

        while True:
            if cur.val != val:
                res.append(cur.val)
            cur = cur.next
            if cur is None:
                break

        result = None
        if len(res) == 0:
            return
        if len(res) == 1:
            return ListNode(res[0])

        is_next = ListNode(res[-1])
        for val in res[-2::-1]:
            result = ListNode(val, is_next)
            is_next = result
        return result


@pytest.mark.parametrize("input_data, expected", [
    ({"head": ListNode(1), "val": 2}, ListNode(1)),
    ({"head": ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), "val": 6},
     ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.removeElements(**input_data) == expected
