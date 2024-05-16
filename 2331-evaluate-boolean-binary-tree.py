# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 1:
            return True
        elif root.val == 2:
            if self.evaluateTree(root.left) or self.evaluateTree(root.right):
                return True
            else:
                return False
        elif root.val == 3:
            if self.evaluateTree(root.left) and self.evaluateTree(root.right):
                return True
            else:
                return False

        return False
