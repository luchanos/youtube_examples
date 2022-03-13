"""
https://leetcode.com/problems/path-sum/submissions/
"""

# Definition for a binary tree node.
from typing import Optional
import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None and targetSum == 0:
            return False
        elif root is None and targetSum != 0:
            return False

        res_from_left = False
        res_from_right = False

        if root.left:
            res_from_left = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            res_from_right = self.hasPathSum(root.right, targetSum - root.val)

        if not root.left and not root.right:
            if targetSum - root.val == 0:
                return True

        if res_from_left or res_from_right:
            return True
        return False


@pytest.mark.parametrize("input_data, expected", [
    ({"root": TreeNode(1, left=TreeNode(2)), "targetSum": 1}, False)
])
def test_remove_element(input_data, expected):
    sol = Solution()
    assert sol.hasPathSum(**input_data) == expected
