"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional

import pytest

from tests.leetcode.easy.utils import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        cur_1_node = list1
        cur_2_node = list2

        if cur_1_node.val < cur_2_node.val:
            res = ListNode(cur_1_node.val)
            cur_1_node = cur_1_node.next
        else:
            res = ListNode(cur_2_node.val)
            cur_2_node = cur_2_node.next
        cur_res_node = res

        while True:
            if cur_1_node is None and cur_2_node is not None:
                next_node = ListNode(cur_2_node.val)
                cur_res_node.next = next_node
                cur_2_node = cur_2_node.next
                cur_res_node = next_node
                continue
            if cur_2_node is None and cur_1_node is not None:
                next_node = ListNode(cur_1_node.val)
                cur_res_node.next = next_node
                cur_1_node = cur_1_node.next
                cur_res_node = next_node
                continue
            if cur_2_node is None and cur_1_node is None:
                break

            if cur_1_node.val < cur_2_node.val:
                next_node = ListNode(cur_1_node.val)
                cur_1_node = cur_1_node.next
            else:
                next_node = ListNode(cur_2_node.val)
                cur_2_node = cur_2_node.next
            cur_res_node.next = next_node
            cur_res_node = next_node
        return res


@pytest.mark.parametrize("input_data, expected", [
    ({"list1": ListNode(1, ListNode(2, ListNode(4))), "list2": ListNode(1, ListNode(3, ListNode(4)))},
     ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))),
    ({"list1": None, "list2": ListNode(2)}, ListNode(2)),
    ({"list1": None, "list2": None}, None),
    ({"list1": ListNode(1), "list2": ListNode(2)}, ListNode(1, ListNode(2))),
    ({"list1": ListNode(-9, ListNode(3)),
      "list2": ListNode(5, ListNode(7))}, ListNode(-9, ListNode(3, ListNode(5, ListNode(7)))))
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.mergeTwoLists(**input_data) == expected
